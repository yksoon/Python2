class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)

def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    # print(name, phone_number, e_mail, addr)
    contact = Contact(name, phone_number, e_mail, addr)
    return contact

# 연락처 출력하기
def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

# 연락처 삭제하기
def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

# 연락처 파일 저장
def store_contact(contact_list):
    f = open("C:/YKSstudy/Python_2/contact_db.txt", "wt", encoding="UTF-8")
    for contact in contact_list:
        f.write(contact.name + "\n")
        f.write(contact.phone_number + "\n")
        f.write(contact.e_mail + "\n")
        f.write(contact.addr + "\n")
    f.close()

# 메인 메뉴 구성하기
def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")

    return int(menu)

# 연락처 불러오기
def load_contact(contact_list):
    f = open("C:/YKSstudy/Python_2/contact_db.txt", "rt", encoding="UTF-8")
    # 파일에서 읽어들인 전체 라인수를 4로 나누어 몇 개의 데이터가 존재하는지 확인
    lines = f.readlines()
    num = len(lines)/4  # 나눗셈 연산을 수행하면 num값이 실수가 되는데,
    num = int(num)      # 이 값을 int() 내장함수를 사용해 정수형으로 형변환

    for i in range(num):
        name = lines[4*i].rstrip("\n")      # rstrip('\n') : 맨 오른쪽 '\'을 제거
        phone = lines[4*i+1].rstrip('\n')   # lstrip('\n') : 맨 왼쪽 '\'을 제거
        email = lines[4*i+2].rstrip('\n')   # strip('\n') : 양쪽 끝의 '\'을 제거
        addr = lines[4*i+3].rstrip('\n')
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    f.close()


# 모듈 자체 테스트 시, 호출할 함수
def run():
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        # 연락처 입력 선택
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)

        # 연락처 출력
        elif menu == 2:
            print_contact(contact_list)

        # 연락처 삭제
        elif menu == 3:
            name = input("Name: ")
            delete_contact(contact_list, name)

        elif menu == 4:
            store_contact(contact_list)
            print("저장 완료")
            print("감사합니다.")
            break

# 모듈 자체 테스트 인지, import 인지를 구분
if __name__ == "__main__":
     run()
