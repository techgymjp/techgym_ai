text = "I have a pen, you have a pen, she has a pen."

from commons.preprocess import Preprocess

preprocess = Preprocess()

preprocess_text = preprocess.process_text(text)

# 各単語にIDを振る
def numbering(text):
  word_list = text.split(" ")
  word_dict = {}
  i = 0
  for word in word_list:
    if word in word_dict.values():
      pass
    else:
      word_dict[i] = word
      i += 1
  return word_dict 

print(text)
print(numbering(preprocess_text))
