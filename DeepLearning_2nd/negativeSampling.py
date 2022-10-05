import numpy as np

print("==============================================")
# 0~9까지의 숫자 중 하나를 선택함
print(np.random.choice(10))
print(np.random.choice(10))

print("==============================================")

words = ['you', 'say','goodbye','I','hello','.']

# words 에서 하나의 단어만 무작위로 샘플링
print(np.random.choice(words))

# words에서 5개의 단어를 무작위로 샘플링(중복 ok)
print(np.random.choice(words, size = 5))

# words에서 5개의 단어를 무작위로 샘플링(중복 no)
print(np.random.choice(words, size = 5, replace=False))

print("==============================================")

# 확률 분포에 따라 샘플링
p = [0.5, 0.1, 0.05, 0.2, 0.05, 0.1]
print(np.random.choice(words, p=p))

print("==============================================")

