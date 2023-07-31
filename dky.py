import json
import random
import threading
import time
import httpx
import os

def get_random_user_agent(user_agents_file_path):
    with open(user_agents_file_path, 'r') as file:
        user_agents = file.readlines()
        return random.choice(user_agents).strip()

def generate_random_data():
    random_number = random.randint(10000000, 99999999)
    email = f'{random_number}@gmail.com'
    data = {
        'email': email,
        'password': str(random_number)
    }
    return data

def post_data(url, user_agents_file_path, success_counter, error_counter):
    user_agent = get_random_user_agent(user_agents_file_path)
    data = generate_random_data()
    headers = {'User-Agent': user_agent, 'Content-Type': 'application/json'}
    
    with httpx.Client(http2=True) as client:
        response = client.post(url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            success_counter.increment()
        else:
            error_counter.increment()
            if 'cf-challenge' in response.text:
                print("  Bị chặn bởi thử thách Cloudflare!")
    
    total_success = success_counter.value
    total_error = error_counter.value
    print(f"  Đăng ký thành công: {total_success} | Lỗi: {total_error}", end='\r')

def send_multiple_requests(domain, user_agents_file_path, num_requests, delay):
    url = f"https://{domain}/api/v1/passport/auth/register"
    
    success_counter = Counter()
    error_counter = Counter()
    
    for _ in range(num_requests):
        thread = threading.Thread(target=post_data, args=(url, user_agents_file_path, success_counter, error_counter))
        thread.start()
        time.sleep(delay)

    total_success = success_counter.value
    total_error = error_counter.value
   # print(f"\n  Đăng ký thành công: {total_success} | Lỗi: {total_error}")

class Counter:
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increment(self):
        with self.lock:
            self.value += 1

# Nhập domain và số interval từ người dùng
os.system("cls" if os.name == "nt" else "clear")
domain = input("\n  Nhập domain: ")
num_requests = int(input("  Nhập số lượng đăng kí: "))
delay = float(input("  Nhập khoảng thời gian giữa các yêu cầu (giây): "))

# Thay thế đường dẫn tới tệp user_agents.txt
user_agents_file_path = 'ua.txt'

send_multiple_requests(domain, user_agents_file_path, num_requests, delay)
