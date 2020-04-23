'''
random.rand() 주어진 형태의 난수 array를 생성

random.randint() [최저값, 최대값]의 범위에서 임의의 정수

random.randn() 표준정규분포(standard normal distribution)를 갖는 난수를 반환

random.standard_normal() : randn()과 standard_normal() 은 기능이 비슷하지만, 
                            standard_normal()은 튜플을 인자로 받는다는 점에서 차이가 있다.
                        
random.random_sample() : [0.0, 1.0) 범위의 임의의 실수를 반환
                          
random.choice() : 주어진 1차원 어레이에서 임의의 샘플을 생성

random.seed() : 난수 생성에 필요한 시드를 정한다. 코드를 실행할 때 마다 똑같은 난수가 생성
'''

# Matplotlib 산점도 그리기
# scatter()를 이용해서 산점도(scatter plot)를 그릴 수 있다.

import matplotlib.pyplot as plt
import numpy as np

'''
np.random.seed() 를 통해서 난수 생성의 시드를 설정하면,
같은 난수를 재사용할 수 있다.

seed() 에 들어갈 파라미터는
0에서 4294967295 사이의 정수여야 한다.
'''

np.random.seed(19680801)

# 1 - rnadom.rand() : 주어진 형태의 난수를 생성

import numpy as np
'''
만들어진 난수 array는 주어진 값에 의해 결정되며,
(0, 1) 범위에서 균일한 분포를 갖는다.
'''
a = np.random.rand(5)
print(a) 
# 결과 : [0.7003673  0.74275081 0.70928001 0.56674552 0.97778533]

'''
x, y의 위치, 마커의 색(colors)과 면적(area)을 무작위로 지정.

예를 들어, x는
[0.7003673  0.74275081, ... ,0.56674552 0.97778533]으로
0에서 1사이의 무작위한 50개 값을 갖는다.
'''
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2

'''
scatter() 에 x, y 위치를 입력
s는 마커의 면적을,
c는 마커의 색을 지정.
alpla는 마커색의 투명도를 결정
'''
plt.scatter(x, y, s = area, c=colors, alpha=0.5)
plt.show()

