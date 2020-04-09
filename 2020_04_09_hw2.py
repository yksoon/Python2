# 1. 사용자한테 이름과 나이를 입력받고, 사용자의 나이가 100살이 되는 연도를
# 화면에 출력하는 프로그램작성.
name = input("이름을 입렵하시오 : ")
age = int(input("나이를 입력하시오 : "))

year = 100 - age + 2020
print(year, "년에 100살 이시네요!")

# 2. 사용자로부터 3개의 숫자를 받아서 평균을 계산하고, 결과를 출력하는 프로그램 완성.
num_1 = int(input("첫 번째 숫자를 입력하시오 : "))
num_2 = int(input("두 번째 숫자를 입력하시오 : "))
num_3 = int(input("세 번째 숫자를 입력하시오 : "))

ave = (num_1 + num_2 + num_3) / 3

print (num_1, num_2, num_3," 의 평균은 ", ave, " 입니다.")

# 3. 사용자로부터 원의 반지름을 입력 받아서 원의 면적을 구하는 프로그램 완성.
radius = int(input("반지름을 입력하시오 : "))
s = 3.14 * radius**2
print("반지름이 ", radius, " 인 원의 넓이 = ", s)

# 4. 원의 반지름을 변수 radius에 저장. radius의 초기값은 50.
# radius 변수를 20씩 증가시키면서 (0, 0) (100, 0) (200, 0) 좌표에 각각 원을 3개 완성.
# 단, 터틀 그래픽을 이용하고, 반복문은 사용하지 않는다.
import turtle
t = turtle.Turtle()

t.shape("turtle")

radius = 50

t.circle(radius)

t.up()
t.goto(100, 0)
t.down()

t.circle(radius + 20)

t.up()
t.goto(200, 0)
t.down()

t.circle(radius + 20 + 20)

# 5. 삼각형의 한 변의 길이를 side 변수로 나타낸다.
# side 변수의 초기값은 100. side 변수를 이용하여 화면에 삼각형을 완성.
import turtle
t = turtle.Turtle()

t.shape("turtle")

side = 100

t.forward(side)

t.left(120)

t.forward(side)

t.left(120)

t.forward(side)

# 6. 5번 문제에서 삼각형의 한 변의 길이를 side 변수로 표시.
# 만약 삼각형 한변의 길이를 200으로 변경한다면 5번 코드에서 어디만 수정하면 되는가?

# 정답 : side = 100  =>  side = 200


# 7. 다음과 같은 그림을 그리는 프로그램을 작성.
# 이 때 작은 사각형의 한 변의 길이는 side 변수에 저장하고, 거북이가 회전하는 각도는 angle 변수에 저장.
import turtle
t = turtle.Turtle()

t.shape("turtle")

side = 100
angle = 90
side_h = side/2

t.forward(side)
t.left(angle)

t.forward(side)
t.left(angle)

t.forward(side)
t.left(angle)

t.forward(side)
t.left(angle)

t.forward(side_h)
t.left(angle)

t.forward(side)
t.left(angle)

t.forward(side_h)
t.left(angle)

t.forward(side_h)
t.left(angle)

t.forward(side)
t.left(angle)

t.left(angle)
t.forward(side_h)

t.left(angle)



