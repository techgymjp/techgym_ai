import numpy as np

class Preprocess():
  def process_text(self, text):
    comma_split = text.split(",")
    comma_text  = "" 
    for i in range(0, len(comma_split) - 1):
      comma_text += comma_split[i] + " ,"
    if (len(comma_split) - 1) > 1:
      comma_text = comma_text + comma_split[len(comma_split) - 1]
    tmp_text   = comma_text
    period_split = tmp_text.split(".")
    period_text  = ""
    for i in range(0, len(period_split) - 1):
      period_text += period_split[i] + " ."
    if (len(period_split) - 1) > 1:
      period_text = period_text + period_split[len(period_split) - 1]

    return period_text

  def numbering(self, text):
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


  # one-hot vectorの作成
  def create_one_hot_vector(self, word_dict):
    one_hot_list = []
    
    for k, word in word_dict.items():
      one_hot = np.zeros(len(word_dict))
      one_hot[k] = 1
      one_hot_list.append(one_hot)

    return np.array(one_hot_list)

  # corpusを作成
  def create_corpus(self, text, word_dict):
    text_list   = text.split(" ")
    number_list = []
    word_dict_swap = {v: k for k, v in word_dict.items()}

    for word in text_list:
      number_list.append(word_dict_swap[word])

    return number_list

  # corpusをone-hot-vectorに変換
  def corpus_to_one_hot_vector(self, corpus, one_hot_vector_list):
    one_hot_vector_corpus = []
    for v in corpus:
      one_hot_vector_corpus.append(one_hot_vector_list[v])
  
    return one_hot_vector_corpus

  # contextとtargetをそれぞれ返す
  def create_context_target(self, corpus):
    contexts = []
    targets  = []
    for i in range(0, len(corpus) - 2):
      contexts.append([corpus[i], corpus[i+2]])
      targets.append(corpus[i+1])
 
    return np.array(contexts), np.array(targets)
