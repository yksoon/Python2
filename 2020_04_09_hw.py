# 1. “환영합니다.” “파이썬의 세계에 오신 것을 환영합니다.” “파이썬은 강력합니다.” 를
# 화면에 출력하는 프로그램작성.
print("환영합니다.")
print("파이썬의 세계에 오신 것을 환영합니다.")
print("파이썬은 강력합니다.")

# 2. 다음 프로그램의 실행 결과를 쓰시오.

# 반갑습니다. 파이썬!!
# 0.6
# Hello world !!!

# 3. 파이썬 쉘을 사용하여 한 주가 몇 시간에 해당하는 지를 계산
print(24 * 7)

# 4. 터틀 그래픽에서 거북이를 이동시켜서 다음과 같은 그림을 완성.
# 단, forward( ), right( ), left( ) 함수만을 사용
import turtle
t = turtle.Turtle()

t.shape("turtle")

t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)

# 5. 터틀 그래픽에서 width( ) 함수를 호출하면 거북이가 그리는 선의 두께를 변경할 수 있다.
# 거북이를 이동하여 다음과 같이 두께가 10인 선을 완성.
import turtle
t = turtle.Turtle()

t.shape("turtle")

t.width(10)

t.forward(100)
t.left(90)
t.forward(100)

# 6. 터틀 그래픽에서 color( ) 함수를 호출하면 거북이가 그리는 선의 색상을 변경할 수 있다.
# 색상을 파랑색으로 변경하여 다음과 같이 길이가 100 pixel 인 선을 완성.
import turtle
t = turtle.Turtle()

t.shape("turtle")

t.color("blue")

t.forward(100)

# 7. 터틀 그래픽에서 shape( )함수를 사용하면 거북이의 모양을 삼각형, 원, 사각형으로 변경할 수 있다.
# 사각형으로 변경하고 100 pixel 길이의 직선완성
import turtle
t = turtle.Turtle()

t.shape("square")

t.forward(100)

# 8. 터틀 그래픽에서 거북이가 이동할 때 선이 그려지지 않게 하려면
# t.up( ) 함수를 이용하여 펜을 들 수 있다.
# 반대로 t.down( ) 함수는 펜을 내려놓는 함수.
# 거북이를 화면 좌표(100, 200)으로 이동 시키려면 t.goto(100, 200) 와 같이 호출.
# 이들 명령어를 조합하여 다음과 같은 그림을 완성.
import turtle
t = turtle.Turtle()

t.shape("turtle")

t.up()
t.goto(100, 100)
t.down()

t.forward(100)

t.up()
t.goto(100, 200)
t.down()

t.forward(100)

# 9. 터틀 그래픽에서 t.circle(100) 이라고 입력 후, 실행하면 화면에 반지름이 100인 원이 그려진다.
# 이들 명령어를 조합하여 화면에 오륜기를 그리는 프로그램 작성.
import turtle
t = turtle.Turtle()

t.shape("turtle")

t.circle(100)

t.up()
t.goto(-100, -120)
t.down()

t.circle(100)

t.up()
t.goto(-190, 0)
t.down()

t.circle(100)

t.up()
t.goto(100, -120)
t.down()

t.circle(100)

t.up()
t.goto(190, 0)
t.down()

t.circle(100)
