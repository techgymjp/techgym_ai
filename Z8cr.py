text = "I have a pen, you have a pen, she has a pen."

# lesson1,2の内容をpreprocessクラスにし、読み込み
from commons.preprocess import Preprocess
import numpy as np

preprocess = Preprocess()

preprocess_text     = preprocess.process_text(text)
numbering_text_dict = preprocess.numbering(preprocess_text)

# one-hot vectorの作成
def create_one_hot_vector(word_dict):
  one_hot_list = []
  
  for k, word in word_dict.items():
    one_hot = np.zeros(len(word_dict))
    one_hot[k] = 1
    one_hot_list.append(one_hot)

  return np.array(one_hot_list)

# 実行結果
print(numbering_text_dict)
print("one-hot vector")
print(create_one_hot_vector(numbering_text_dict))
