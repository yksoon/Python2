import numpy as np

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
matrix2 = np.array(matrix, int).shape # (3, 4)
type(matrix2) # tuple
type(matrix) # list

tensor = [[[1,2,3,4],[5,6,7,8],[9,10,11,12]],
          [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
          [[1,2,3,4],[5,6,7,8],[9,10,11,12]]]

np.array(tensor, int).shape # (3, 3, 4)

np.array([[1,2.6,3.2], [4,5.1,6]], dtype=int)

np.array( [[1,2.6, 3.2], [4, "5", 6]], dtype=np.float32)
#array([[1. , 2.6, 3.2],
#       [4. , 5. , 6. ]], dtype=float32)

np.array([[1,2.6,3.2], [4,5.1,6]], dtype=np.float32).nbytes
# 24

np.array([[1,2.6,3.2], [4,5.1,6]], dtype=np.float64).nbytes
# 48

np.array([[1,2.6,3.2], [4,5.1,6]], dtype=np.int8).nbytes
# 6



t_matrix = [[1,2,3,4], [5,6,7,8]]
np.array(t_matrix).shape
# (2, 4)
np.array(t_matrix).reshape(8,)
# array([1, 2, 3, 4, 5, 6, 7, 8])
np.array(t_matrix).reshape(8,).shape
# (8,)


np.array(t_matrix).reshape(2,4).shape
# (2, 4)
np.array(t_matrix).reshape(-1,2).shape
# (4, 2)
np.array(t_matrix).reshape(2,2,2)


t_matrix = [[[1,2], [3,4]],[[1,2],[3,4]],[[1,2],[3,4]]]
np.array(t_matrix).flatten()

a = np.array([[1,2.2,3],[4,5,6.3]],int)
print(a)

print(a[0,0])

print(a[0][0])

a[0,0] = 7
print(a)




a = np.array([[1,2,3,4,5], [6,7,8,9,10]],int)

a[:, 1:]
a[1, 2:4]
a[1:3]

a = np.array([[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]],int)
print(a)

a[:,::2] # 행과 열은 내부 인덱스를 뽑는거고, 두 번째는 위치를 뽑는것
#array([[ 0,  2,  4],
#       [ 5,  7,  9],
#       [10, 12, 14]])

a[::2,::2] # ::은 스텝(간격)을 의미한다.
#array([[ 0,  2,  4],
#       [10, 12, 14]])

np.arange(20) # list의 range와 같은 역할, intege로 0부터 10까지 배열 추출

np.arange(0,1,0.2) # float 가능

np.arange(20).reshape(4,5)


np.zeros(shape = (5,2), dtype = np.int8) # 5 by 2 zero matrix생성, int8

np.ones(shape = (5,2), dtype = np.int8) # 5 by 2 one matrix생성, int8


np.empty(shape=(3,2), dtype = np.int8)

'''
empty는 주어진 shape대로 비어있는 것을 생성한다.
이런식으로 array를 만드는데 메모리를 어느 정도 할당 시켜준다.
그런데 메모리에 기존에 있었던 값을 보여준다.
'''

'''
zeros나 ones는 0과 1로 메모리 할당 값을 초기화 시켜주는데
empty는 초기화시키지 않고 기존에 메모리에 있는 찌꺼기 그대로 보여준다.
'''

# - 기존 ndarray의 shape 크기만큼 1 or 0 or empty array 반환
t_matrix = np.arange(15).reshape(3,5)
np.ones_like(t_matrix)

t_matrix = np.arange(15).reshape(3,5)
np.zeros_like(t_matrix)

t_matrix = np.arange(15).reshape(3,5)
np.empty_like(t_matrix)


# - 단위 행렬(i행렬)을 생성
np.identity(n=3,dtype = np.int8)

np.identity(n=5)

np.eye(N = 3, M = 4, dtype=np.int)

np.eye(4)   # identity 행렬과 같게 출력

np.eye(3, 6, k=3)   # k -> start index



# - 대각선 값만 반환시켜주는 함수
t_matrix = np.arange(16).reshape(4,4)
np.diag(t_matrix)

np.diag(t_matrix, k=1)


##-----


np.random.uniform(0,1,12).reshape(4,3)  # 균등분포
# np.random.uniform(최소값, 최대값, data개수)

np.random.normal(0,1,12).reshape(4,3) # 정규분포




##---------

# - 모든 operation function을 실행할 때, 기준이 되는 dimension 축
t_array = np.arange(1, 13).reshape(3,4)
t_array

t_array.sum(axis=0), t_array.sum(axis=1)


tensor = np.array([t_array, t_array, t_array])
tensor


t_array = np.arange(1, 13).reshape(3,4)
t_array

t_array.mean(), t_array.mean(axis=0)

t_array.std(), t_array.std(axis=0)


np.exp(t_array) # 지수함수

np.sqrt(t_array) # 루트

np.sin(t_array) # sin함수



# - Numpy array를 합치는 함수
a = np.array([1,2,3])
b = np.array([4,5,6])
np.vstack((a,b))

a = np.array([[1], [2], [3]])
b = np.array([[4], [5], [6]])
np.hstack((a,b))


a = np.array([[1,2,3]])
b = np.array([[4,5,6]])
np.concatenate((a,b), axis=0)

a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
np.concatenate((a,b.T), axis=1) # a.T는 a의 역행렬


a = np.array([[1,2,3], [4,5,6]], float)
a + a

a - a

a * a


dot_a = np.arange(1,7).reshape(2,3)
dot_b = np.arange(1,7).reshape(3,2)
dot_a.dot(dot_b)


t_matrix = np.array([[1,2],[3,4]], float)
scalar = 2
t_matrix + scalar   # matrix, scalar 덧셈

t_matrix = np.arange(1,13).reshape(4,3)
t_vector = np.arange(100,400,100)
t_matrix + t_vector



a = np.arange(5)
a

np.all(a>3)

np.all(a<5)

np.any(a>3)

np.any(a>5)


a = np.array([1,5,3], float)
b = np.array([4,7,2], float)
a>b

a == b

(a>b).any()

(a>b).all()



a = np.array([2,3,1], float)
np.logical_and(a>0, a<3)

b = np.array([False, True, True], bool)
np.logical_not(b)

c = np.array([False, False, False], bool)
np.logical_or(b,c)




a = np.array([2,3,1], float)
np.where(a > 1, 0, 3)

a = np.arange(3, 10)
np.where(a > 6)     # True 값의 index 반환

a = np.array([2, np.NaN, np.Inf], float)
np.isnan(a) # null인 경우 True

np.isfinite(a)  # 한정된 수인 경우 True



## argmax, argmin
# - array내 최대값 또는 최소값의 index 반환
a = np.array([2,3,1,5,6,22,11])
np.argmax(a), np.argmin(a)

# - axis 기반의 반환
a = np.array([[1,4,2,22], [45,32,4,7], [34,54,9,8]])
np.argmax(a, axis=0), np.argmin(a, axis=1)




'''
numpy의 배열은 특정 조건에 따른 값을 배열 형태로 추출 가능
comparison operation 함수들도 모두 사용 가능
'''
t_a = np.array([3,5,8,0,7,4], float)
t_a > 4

t_a[t_a > 4]   # 조건이 True인 index의 요소값만 추출

t_c = t_a < 4
t_c

t_a[t_c]

