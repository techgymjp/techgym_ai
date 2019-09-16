text = "I have a pen, you have a pen, she has a pen."

# lesson1,2,4,5の内容をpreprocessクラスにし、読み込み
from commons.preprocess  import Preprocess
from commons.simple_cbow import SimpleCBOW
from commons.trainer     import Trainer
from commons.optimizer   import Adam
import numpy as np



preprocess = Preprocess()

window_size = 1
hidden_size = 5
batch_size  = 3
max_epoch   = 1000

preprocess_text       = preprocess.process_text(text)
numbering_text_dict   = preprocess.numbering(preprocess_text)
preprocess_text       = preprocess.process_text(text)
one_hot_vector_list   = preprocess.create_one_hot_vector(numbering_text_dict)
corpus                = preprocess.create_corpus(preprocess_text, numbering_text_dict)
one_hot_vector_corpus = preprocess.corpus_to_one_hot_vector(corpus, one_hot_vector_list)
contexts, targets     = preprocess.create_context_target(one_hot_vector_corpus)

vocab_size = len(numbering_text_dict)

# modelの利用
model     = SimpleCBOW(vocab_size, hidden_size)
optimizer = Adam()
trainer   = Trainer(model, optimizer)
trainer.fit(contexts, targets, max_epoch, batch_size)
# trainer.plot()

# word vectorの確認
word_vecs = model.word_vecs
for word_id, word in numbering_text_dict.items():
  print(word, word_vecs[word_id])
