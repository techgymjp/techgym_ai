text = "I have a pen, you have a pen, she has a pen."

# lesson1,2の内容をpreprocessクラスにし、読み込み
from commons.preprocess import Preprocess
import numpy as np

preprocess = Preprocess()

preprocess_text     = preprocess.process_text(text)
numbering_text_dict = preprocess.numbering(preprocess_text)

# 共起行列の作成
def create_co_matrix(text, word_dict):

# 実行結果
print(text)
print(numbering_text_dict)
print("共起行列")
print(create_co_matrix(preprocess_text, numbering_text_dict))
