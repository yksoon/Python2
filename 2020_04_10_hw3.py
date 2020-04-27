# 문제 7-1
# 1 부터 10 까지의 숫자를 각 라인 단위로 파일에 출력하는 프로그램을 작성하세요. 생성되는 파일의 이름은 number.txt 이다.

f = open("number.txt", "wt")

for i in range(1,11):
    f.write("%d \n" % i)

f.close()

# 문제 7-2
# 사용자로부터 경로를 입력 받은 후 해당 경로에 있는 디렉터리와 파일 목록을 flist.txt 라는 파일로 출력하는 함수를 작성하세요.
import os

file = os.listdir("/Users/yong-kwangsoon/Desktop/YKS_project/Python2/")
print(file)
f = open("flist.txt", "wt")

# print(len(file))

for i in range(len(file)):
    f.write("%s \n" % file[i])
f.close()