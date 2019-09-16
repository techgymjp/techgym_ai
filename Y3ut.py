text = "I have a pen, you have a pen, she has a pen."

# lesson1の内容をpreprocessクラスにし、読み込み
from commons.preprocess import Preprocess

preprocess = Preprocess()

preprocess_text = preprocess.process_text(text)

# 各単語にIDを振る
def numbering(text):

# 実行結果
print(text)
print(numbering(preprocess_text))
