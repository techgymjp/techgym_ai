text = "I have a pen, you have a pen, she has a pen."

# lesson1,2,4の内容をpreprocessクラスにし、読み込み
from commons.preprocess import Preprocess
import numpy as np

preprocess = Preprocess()

preprocess_text     = preprocess.process_text(text)
numbering_text_dict = preprocess.numbering(preprocess_text)
one_hot_vector_list = preprocess.create_one_hot_vector(numbering_text_dict)

# corpusを作成
corpus = preprocess.create_corpus(preprocess_text, numbering_text_dict)

# corpusをone-hot-vectorに変換
def corpus_to_one_hot_vector(corpus, one_hot_vector_list):
  one_hot_vector_corpus = []
  for v in corpus:
    one_hot_vector_corpus.append(one_hot_vector_list[v])
  
  return one_hot_vector_corpus

# contextとtargetをそれぞれ返す
def create_context_target(corpus):
  contexts = []
  targets  = []
  for i in range(0, len(corpus) - 2):
    contexts.append([corpus[i], corpus[i+2]])
    targets.append(corpus[i+1])
 
  return np.array(contexts), np.array(targets)

# 実行結果
print("text")
print(text)
print("corpus")
print(corpus)
one_hot_vector_corpus = corpus_to_one_hot_vector(corpus, one_hot_vector_list)
contexts, targets = create_context_target(one_hot_vector_corpus)
print("contexts")
print(contexts)
print("target")
print(targets)
