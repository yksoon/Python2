"""
문제 4-1
아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.
참고로 print('*', end='')와 같이 print 함수를 사용하면 줄바꿈 없이 화면에 출력할 수 있습니다.
*****
"""

for i in range(5):
    print('*', end='')

"""
문제 4-2
아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해보세요.
(힌트: 중첩 루프 사용)
"""

for i in range(3):
    print()
    for n in range(5):
        print("*", end='')
        
"""
문제 4-3
아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해보세요.
*
**
***
****
*****
"""

for i in range(6):
    print("*"*i)

"""
문제 4-4
아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.
*****
****
***
**
*
"""
print()
for i in range(5):
    for n in range(5 -i):
        print("*", end="")
    print()

print()
"""
문제 4-5
아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.
    *
   **
  ***
 ****
*****
"""

for i in range(1, 6):
    for n in range(5-i):
        print(" ",end="")
    for n in range(i):
        print("*",end="")
    print()

print()
"""
문제 4-6
아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.
*****
 ****
  ***
   **
    *
"""
for i in range(5):
    for n in range(i):
        print(" ",end="")
    for n in range(5-i):
        print("*",end="")
    
    print()

print()
"""
문제 4-7
아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.
    *  1 - 1
   *** 2 - 3
  *****3 - 5
 *******4 -7
*********5 -9
"""
for i in range(6):
    for n in range(5-i):
        print(" ", end="")
    for n in range(2*i-1):
        print("*",end="")
    print()

print()
"""
문제 4-8
아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성 해보세요.
*********
 *******
  *****
   ***
    *
"""
for i in range(6):
    for n in range(i):
        print(" ", end="")
    for n in range(2*(5-i)-1):
        print("*",end="")
    print()

"""
문제 4-9
중첩 루프를 이용해 신문 배달을 하는 프로그램을 작성하세요.
단, 아래에서 arrears 리스트는
신문 구독료가 미납된 세대에 대한 정보를 포함하고 있는데,
해당 세대에는 신문을 배달하지 않아야 합니다.
>>> apart = [[101, 102, 103, 104],[201, 202, 203, 204],[301, 302, 303, 304], [401, 402, 403, 404]]
>>> arrears = [101, 203, 301, 404]
"""

apart = [[101, 102, 103, 104],[201, 202, 203, 204],[301, 302, 303, 304], [401, 402, 403, 404]]

for floor in apart:
    for room in floor:
        if room == 101:
            print("미납")
        if room == 203:
            print("미납")
        if room == 301:
            print("미납")
        if room == 404:
            print("미납")
        else:
            print("배달 완료 : ", room)
        





