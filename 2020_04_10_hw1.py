# 연습문제

# 문제 5-1
# 두 개의 정수 값을 받아 두 값의 평균을 구하는 함수를 작성하세요.

def myaverage(a, b):
    c = (a + b) / 2
    return c

# 문제 5-2
# 함수의 인자로 리스트를 받은 후 리스트 내에 있는 모든 정수 값에 대한 최댓값과 최솟값을 반환하는
# 함수를 작성하세요.

def get_max_min(data_list):
    list_max = max(data_list)
    list_min = min(data_list)

    return (list_max, list_min)

# 문제 5-3
# 절대 경로를 입력받은 후 해당 경로에 있는 *.txt 파일의 목록을 파이썬 리스트로 반환하는 함수를
# 작성하세요.

import os
def get_txt_list(path):
    
    txt=[]
    for x in os.listdir(path):
        if x.endswith('txt'):
            txt.append(x)
            
    return txt

print(get_txt_list(input("디렉터리 입력 : ")))


# 5-4

def bmidef(weight, height_cm):
    bmi = weight / (height_cm * 0.01)**2

    result = ""
    if bmi < 18.5:
        result = "마른체형"
    elif 18.5 <= bmi < 25.0:
        result = "표준"
    elif 25.0 <= BMI < 30.0:
        result = "비만"
    elif BMI >= 30.0:
        result = "고도비만"

    return result

# 문제 5-5
# 사용자로부터 키(cm)와 몸무게(kg)를 입력받은 후 BMI 값과 BMI 값에 따른 체형 정보를 화면에 출력하는
# 프로그램을 작성해 보세요. 파이썬에서 사용자로부터의 입력은 input() 함수를 사용하며, 작성된 프로그램은
# 계속해서 사용자로부터 키와 몸무게를 입력받은 후 BMI 및 체형 정보를 출력해야 합니다(무한 루프 구조).

while 1:
    weight = int(input("체중을 입력하세요 : "))
    height_cm = int(input("키를 입력하세요 : "))

    print(bmidef(weight, height_cm))


# 문제 5-6
# 삼각형의 밑변과 높이를 입력받은 후 삼각형의 면적을 계산하는 함수를 작성하세요.

def get_triangle_area(width, height):
    area = width * height / 2

    return area

width = int(input("밑변 입력 : "))
height = int(input("높이 입력 : "))

print("삼각형의 넓이 : ", get_triangle_area(width, height))

# 문제 5-7
# 함수의 인자로 시작과 끝 숫자를 받아 시작부터 끝까지의 모든 정수값의 합을 반환하는 함수를
# 작성하세요(시작값과 끝값을 포함).

def add_start_to_end(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i

    return sum

start = int(input("시작 값 : "))
end = int(input("끝 값 : "))
print("모든 정수의 합 : ", add_start_to_end(start, end))


# 문제 5-8
# 함수의 인자로 문자열을 포함하는 리스트가 입력될 때 각 문자열의 첫 세 글자로만 구성된 리스트를
# 반환하는 함수를 작성하세요. 예를 들어, 함수의 입력으로 ['Seoul', 'Daegu', 'Kwangju', 'Jeju']가 입력될 때
# 함수의 반환값은 ['Seo', 'Dae', 'Kwa', 'Jej']입니다.

def word_3(word):
    s = word[:3]
    return s

word = input("단어 입력 : ")
print(word_3(word))


