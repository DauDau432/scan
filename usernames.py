import random
import string
import os
from os import name, system

if name == 'nt':
    system("title Đậu Đậu - Tạo Tên Người Dùng")
    system("mode 90, 25")
def generate_random_digits():
    return ''.join(random.choices(string.digits, k=random.randint(1, 9)))

def generate_username():
    countries = {
        'Vietnam': [
            'Nguyen', 'Tran', 'Le', 'Pham', 'Huynh', 'Hoang', 'Phan', 'Vu', 'Vo', 'Dang', 'Bui', 'Do', 'Ho', 'Ngo', 'Duong', 'Ly',
            'Thi', 'Ngoc', 'Quyen', 'An', 'Bach', 'Bang', 'Binh', 'Canh', 'Dinh', 'Giang', 'Han', 'Khanh', 'Khoa', 'Lam', 'Mai',
            'Ninh', 'Quoc', 'Quy', 'Tan', 'Thai', 'Thien', 'Tien', 'Tin', 'Trong', 'Tuan', 'Tung', 'Van', 'Vinh', 'Xuan'
        ],
        'United States': [
            'Smith', 'Johnson', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Martinez', 'Wilson', 'Anderson', 'Taylor',
            'Thomas', 'Hernandez', 'Moore', 'Martin', 'Jackson', 'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez',
            'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker', 'Young', 'Allen', 'King', 'Wright', 'Scott', 'Torres',
        ],
        'Japan': [
            'Ichiro', 'Jiro', 'Saburo', 'Shiro', 'Goro', 'Rokuro', 'Shichiro', 'Hachiro', 'Kichiro', 'Junko', 'Hiroko', 'Eiko',
            'Akiko', 'Keiko', 'Emi', 'Yumi', 'Ayumi', 'Asuka', 'Naoko', 'Kaori', 'Yoko', 'Kyoko', 'Hana', 'Sakura', 'Koharu',
            'Haru', 'Aoi', 'Kaito', 'Haruki', 'Riku', 'Ren', 'Yuto', 'Haruto', 'Sota', 'Yuki', 'Aya', 'Yui', 'Mayu', 'Rina',
        ],
        # Thêm các quốc gia khác vào đây nếu muốn
    }

    country = random.choice(list(countries.keys()))
    first_name = random.choice(countries[country])
    random_numbers = generate_random_digits()

    username = f"{first_name}{random_numbers}"
    return username
# os.system("cls" if os.name == "nt" else "clear")
def save_usernames_to_file(file_path):
    count = 0
    banner = r'''
  .S       S.     sSSs    sSSs   .S_sSSs     .S_sSSs     .S_SSSs     .S_SsS_S.     sSSs  
 .SS       SS.   d%%SP   d%%SP  .SS~YS%%b   .SS~YS%%b   .SS~SSSSS   .SS~S*S~SS.   d%%SP  
 S%S       S%S  d%S'    d%S'    S%S   `S%b  S%S   `S%b  S%S   SSSS  S%S `Y' S%S  d%S'    
 S%S       S%S  S%|     S%S     S%S    S%S  S%S    S%S  S%S    S%S  S%S     S%S  S%S     
 S&S       S&S  S&S     S&S     S%S    d*S  S%S    S&S  S%S SSSS%S  S%S     S%S  S&S     
 S&S       S&S  Y&Ss    S&S_Ss  S&S   .S*S  S&S    S&S  S&S  SSS%S  S&S     S&S  S&S_Ss  
 S&S       S&S  `S&&S   S&S~SP  S&S_sdSSS   S&S    S&S  S&S    S&S  S&S     S&S  S&S~SP  
 S&S       S&S    `S*S  S&S     S&S~YSY%b   S&S    S&S  S&S    S&S  S&S     S&S  S&S      
 S*b       d*S     l*S  S*b     S*S   `S%b  S*S    S*S  S*S    S&S  S*S     S*S  S*b     
 S*S.     .S*S    .S*P  S*S.    S*S    S%S  S*S    S*S  S*S    S*S  S*S     S*S  S*S.    
  SSSbs_sdSSS   sSS*S    SSSbs  S*S    S&S  S*S    S*S  S*S    S*S  S*S     S*S   SSSbs  
   YSSP~YSSY    YSS'      YSSP  S*S    SSS  S*S    SSS  SSS    S*S  SSS     S*S    YSSP  
                                SP          SP                 SP           SP           
                                Y           Y                  Y            Y                                                                                           
'''
    print(banner)

    with open(file_path, 'a') as file:
        try:
            while True:
                username = generate_username()
                file.write(username + '\n')
                count += 1
                print(f"  Số lượng tên đã tạo: {count}", end='\r')
        except KeyboardInterrupt:
            print("\n  Đã dừng tạo tên người dùng.")

if __name__ == "__main__":
    file_path = 'usernames.txt'
    save_usernames_to_file(file_path)
