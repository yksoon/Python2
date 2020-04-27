class Board:
    def __init__(self, no, author, title, content, hit):
        self.no = no
        self.title = title
        self.content = content
        self.author = author
        self.hit = hit
    
    def print_info(self):
        print("======================")
        print("글번호 : ", self.no)
        print("제목 : ", self.title)
        print("조회수 : ", self.hit)
        print("----------------------")
        print("작성자 : ", self.author)
        print(self.content)
        print("======================")
        print()

        back = input("메뉴로 가려면 'enter'를 입력하세요.")
        
# 메인메뉴 구성
def print_menu():
    f = open("board_db.txt", "rt")
    # 파일에서 읽어들인 전체 라인수를 5로 나누어 몇 개의 데이터가 존재하는지 확인
    lines = f.readlines()
    num = len(lines)/5  # 나눗셈 연산을 수행하면 num값이 실수가 되는데,
    num = int(num)      # 이 값을 int() 내장함수를 사용해 정수형으로 형변환

    for i in range(num):
        no = lines[5*i].rstrip("\n")      # rstrip('\n') : 맨 오른쪽 '\'을 제거
        author = lines[5*i+1].rstrip('\n')   # lstrip('\n') : 맨 왼쪽 '\'을 제거
        title = lines[5*i+2].rstrip('\n')   # strip('\n') : 양쪽 끝의 '\'을 제거
        content = lines[5*i+3].rstrip('\n')
        hit = lines[5*i+4].rstrip('\n')
        # print(lines)
        # print(i)
        print("| 글번호 : {} | 작성자 : {} | 제목 : {} |".format(no, author, title))
    
    print()
    menu = input("| 게시판 확인 : '글번호' 입력 | 게시판 작성 : 'add' 입력 | 게시판 종료 : 'exit' 입력 | : ")
    return menu

# 게시판 작성
def set_board():
    f = open("board_db.txt", "rt")
    # 파일에서 읽어들인 전체 라인수를 5로 나누어 몇 개의 데이터가 존재하는지 확인
    lines = f.readlines()
    num = len(lines)/5  # 나눗셈 연산을 수행하면 num값이 실수가 되는데,
    num = int(num)      # 이 값을 int() 내장함수를 사용해 정수형으로 형변환

    no = 0
    if lines[0] == None:
        no = "0"
    else:
        no = lines[5*num-5]
        no = str(int(no.rstrip("\n")) + 1)
    author = input("작성자: ")
    title = input("제목: ")
    content = input("내용: ")
    hit = "0"

    board = Board(no, author, title, content, hit)
    
    return board

# 게시판 파일 저장
def store_board(board_list):
    f = open("board_db.txt", "wt")
    for board in board_list:
        f.write(board.no + "\n")
        f.write(board.author + "\n")
        f.write(board.title + "\n")
        f.write(board.content + "\n")
        f.write(board.hit + "\n")
    f.close()

# 게시판 불러오기
def load_board(board_list):
    f = open("board_db.txt", "rt")
    # 파일에서 읽어들인 전체 라인수를 5로 나누어 몇 개의 데이터가 존재하는지 확인
    lines = f.readlines()
    num = len(lines)/5  # 나눗셈 연산을 수행하면 num값이 실수가 되는데,
    num = int(num)      # 이 값을 int() 내장함수를 사용해 정수형으로 형변환

    for i in range(num):
        no = lines[5*i].rstrip("\n")      # rstrip('\n') : 맨 오른쪽 '\'을 제거
        author = lines[5*i+1].rstrip('\n')   # lstrip('\n') : 맨 왼쪽 '\'을 제거
        title = lines[5*i+2].rstrip('\n')   # strip('\n') : 양쪽 끝의 '\'을 제거
        content = lines[5*i+3].rstrip('\n')
        hit = lines[5*i+4].rstrip('\n')
        board = Board(no, author, title, content, hit)
        board_list.append(board)

    f.close()

def choose_board(menu, board_list):
    try:
        f = open("board_db.txt", "r+")
        
        # 파일에서 읽어들인 전체 라인수를 5로 나누어 몇 개의 데이터가 존재하는지 확인
        lines = f.readlines()
        
        num = menu
        num = int(num)

        no = lines[5*num-5].rstrip("\n")   # rstrip('\n') : 맨 오른쪽 '\'을 제거
        author = lines[5*num-4].rstrip('\n')   # lstrip('\n') : 맨 왼쪽 '\'을 제거
        title = lines[5*num-3].rstrip('\n')   # strip('\n') : 양쪽 끝의 '\'을 제거
        content = lines[5*num-2].rstrip('\n')
        hit = lines[5*num-1].rstrip('\n')


        board = Board(no, author, title, content, hit)

        board.print_info()

        f.close()
    
    except ValueError:
        pass

# 게시판 출력하기
def print_board(board_list):
    for board in board_list:
        board.print_info()

def run():
    board_list = []
    load_board(board_list)

    while 1:
        menu = print_menu()

        if menu == 1:
            print_board(board_list)
        
        # 게시판 입력
        elif menu == "add":
            board = set_board()
            board_list.append(board)
            store_board(board_list)
            print()
            print("저장되었습니다.")
            print()
        
        # 종료
        elif menu == "exit":
            break

        # 게시판 출력
        else:
            choose_board(menu, board_list)
        
        

if __name__ == "__main__":
    run()
        