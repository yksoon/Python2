# 문제 6-1
# 다음의 조건을 만족하는 Point 라는 클래스를 작성하세요.
# - Point 클래스는 생성자를 통해 (x, y) 좌표를 입력받는다.
# - setx(x), sety(y) 메서드를 통해 x 좌표와 y 좌표를 따로 입력받을 수도 있다.
# - get() 메서드를 호출하면 튜플로 구성된 (x, y) 좌표를 반환한다.
# - move(dx, dy) 메서드는 현재 좌표를 dx, dy 만큼 이동시킨다.
# - 모든 메서드는 인스턴스 메서드다.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y
    
    def get(self):
        return (self.x, self.y)
    
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

# 문제 6-2
# 문제 6-1 에서 생성한 Point 클래스에 대한 인스턴스를 생성한 후 4 개의 메서드를 사용하는 코드를 작성하세요.

p = Point(10, 20)
print(p.get())
p.setx(20)
print(p.get())
p.sety(30)
print(p.get())
p.move(20, 20)
print(p.get())

# 문제 6-3
# 아래의 Stock 클래스에 대해 2 개의 인스턴스를 생성했을 때 클래스와 a 와 b 인스턴스의 네임스페이스를 그려보세요.

class Stock:
    market = "Kospi"

a = Stock()
b = Stock()

print(a.__dict__)
print(b.__dict__)

# 문제 6-4
# 문제 6-3 의 코드에서 추가로 아래와 같은 코드를 수행했을 때 '???'로 표시된 부분의 결괏값을 적어보세요.
print(a.market)
print(b.market)
print(Stock.market)
a.market = "Kosdaq"
b.market = "Nasdaq"
print(a.market)
print(b.market)
print(Stock.market)

# 문제 6-5
# 문제 6-3, 문제 6-4 의 코드가 모두 수행된 후의 Stock 클래스, a 인스턴스와 b 인스턴스의 네임스페이스를 그려보세요.

# a.market => "Kosdaq"
# b.market => "Nasdaq"
# Stock.market => "Kospi"