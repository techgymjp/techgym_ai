text = "I have a pen, you have a pen, she has a pen."

# lesson1,2の内容をpreprocessクラスにし、読み込み
from commons.preprocess import Preprocess
import numpy as np

preprocess = Preprocess()

preprocess_text     = preprocess.process_text(text)
numbering_text_dict = preprocess.numbering(preprocess_text)

# 共起行列の作成
def create_co_matrix(text, word_dict):
  co_matrix   = np.zeros((len(word_dict), len(word_dict)))
  text_list   = text.split(" ")
  number_list = []
  word_dict_swap = {v: k for k, v in word_dict.items()}

  for word in text_list:
    number_list.append(word_dict_swap[word]) 

  for i, word_id in enumerate(number_list):
    if i > 0:
      left  = i - 1
      left_word_id = number_list[left]
      co_matrix[word_id, left_word_id] = 1
    
    if i < len(number_list) - 1:
      right = i + 1
      right_word_id = number_list[right]
      co_matrix[word_id, right_word_id] = 1

  return co_matrix

# 実行結果
print(text)
print(numbering_text_dict)
print("共起行列")
print(create_co_matrix(preprocess_text, numbering_text_dict))
