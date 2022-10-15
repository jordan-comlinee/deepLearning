import sys
sys.path.append('..')
from common.util import preprocess, create_co_matrix, cos_similarity

text = 'You say goodbye and I say hello.'
corpus, word_to_id, id_to_word = preprocess(text)
vocab_size = len(word_to_id)
C = create_co_matrix(corpus, vocab_size)

# you 의 단어 벡터
c0 = C[word_to_id['you']]
print("you: ", c0)
# i의 단어 벡터
c1 = C[word_to_id['i']]
print("i: ", c1)

print(cos_similarity(c1, c1))