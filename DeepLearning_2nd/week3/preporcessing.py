import numpy as np

text = 'You say goodbye and I say hello.'
# 대문자를 소문자로 치환
text = text.lower()
# .을 따로 구분함
text = text.replace('.', ' .')
# 띄어쓰기를 단위로 단어를 구분함
words = text.split(' ');

print(words)

word_to_id = {}
id_to_word = {}

for word in words :
    # 만약 word_to_id 딕셔너리에 word가 없다면
    if word not in word_to_id:
        # 새로운 id 생성
        new_id = len(word_to_id)
        # word_to_id에 word에 대한 id 값 대응
        word_to_id[word] = new_id
        # id_to_word 에 id에 대한 word 값 대응
        id_to_word[new_id] = word

print(id_to_word)
print(word_to_id)

corpus = [word_to_id[w] for w in words]
print(corpus)
corpus = np.array(corpus)
print(corpus)

