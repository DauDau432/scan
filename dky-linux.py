# chương trình đăng kí tài khoản v2board số lượng lớn
import json
import random
import threading
import time
import httpx
import os
import sys
from os import name, system
if name == 'nt':
    system("title Đậu Đậu - Đăng Ký Tài Khoản V2board SLL")
    system("mode 55, 15")
def get_random_user_agent(user_agents_file_path):
    with open(user_agents_file_path, 'r') as file:
        user_agents = file.readlines()
        return random.choice(user_agents).strip()

def generate_random_data(usernames_file_path):
    with open(usernames_file_path, 'r') as file:
        usernames = file.readlines()
        random_username = random.choice(usernames).strip()

    email = f'{random_username}@gmail.com'
    data = {
        'email': email,
        'password': str(random_username)
    }
    return data

def post_data(url, usernames_file_path, user_agents_file_path, success_counter, error_counter):
    user_agent = get_random_user_agent(user_agents_file_path)
    data = generate_random_data(usernames_file_path)
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
        thread = threading.Thread(target=post_data, args=(url, usernames_file_path, user_agents_file_path, success_counter, error_counter))
        thread.start()
        time.sleep(delay)

    total_success = success_counter.value
    total_error = error_counter.value

class Counter:
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increment(self):
        with self.lock:
            self.value += 1

def check_file_existence(file_path):
    return os.path.exists(file_path)

# Hàm để yêu cầu người dùng nhấn Enter để thoát
def nhan_enter_de_thoat():
    input("\n\n  Nhấn Enter để thoát...")

# Nhập domain và số interval từ người dùng
def nhap_tham_so_tu_dong_lenh():
    if len(sys.argv) != 4:
        print("  Sử dụng: python dky.py domain requests delay")
        exit(1)

    domain = sys.argv[1]
    num_requests = int(sys.argv[2])
    delay = float(sys.argv[3])

    return domain, num_requests, delay

if __name__ == "__main__":
    domain, num_requests, delay = nhap_tham_so_tu_dong_lenh()

    # Kiểm tra sự tồn tại của tệp ua.txt
    user_agents_file_path = 'ua.txt'
    if not check_file_existence(user_agents_file_path):
        print(f"  file {user_agents_file_path} không tồn tại. Vui lòng kiểm tra lại!")
        exit(1)

    # Kiểm tra sự tồn tại của tệp usernames.txt
    usernames_file_path = 'usernames.txt'
    if not check_file_existence(usernames_file_path):
        print(f"  file {usernames_file_path} không tồn tại. Vui lòng kiểm tra lại!")
        exit(1)

    send_multiple_requests(domain, user_agents_file_path, num_requests, delay)

    # Yêu cầu người dùng nhấn Enter trước khi thoát
    nhan_enter_de_thoat()