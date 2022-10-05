import numpy as np

W = np.arange(21).reshape(7, 3)

print(W)

print(W[2])
print(W[5])


# 가중치 W로부터 여러 개의 행을 한꺼번에 추출

idx = np.array([1, 0, 3, 0])

print(W[idx])