from __future__ import absolute_import, division, print_function, unicode_literals

# tensorflowライブラリの読み込み
import tensorflow_datasets as tfds
import tensorflow as tf


# データセットの読み込み

tokenizer = info.features['text'].encoder

BUFFER_SIZE = 10000
BATCH_SIZE  = 64

# 特定のバッチサイズを抽出
train_dataset = train_dataset.shuffle(BUFFER_SIZE)
train_dataset = train_dataset.padded_batch(BATCH_SIZE, train_dataset.output_shapes)
test_dataset  = test_dataset.padded_batch(BATCH_SIZE, test_dataset.output_shapes)

# モデルの構築

# 学習
history = model.fit(train_dataset, epochs=10,
                    validation_data=test_dataset)

test_loss, test_acc = model.evaluate(test_dataset)

# サポート用メソッド
def pad_to_size(vec, size):
  zeros = [0] * (size - len(vec))
  vec.extend(zeros)
  return vec

def sample_predict(sentence, pad):
  tokenized_sample_pred_text = tokenizer.encode(sample_pred_text)

  if pad:
    tokenized_sample_pred_text = pad_to_size(tokenized_sample_pred_text, 64)

  predictions = model.predict(tf.expand_dims(tokenized_sample_pred_text, 0))

  return (predictions)

# 実行例
sample_pred_text = ('The movie was cool. The animation and the graphics '
                    'were out of this world. I would recommend this movie.')
predictions = sample_predict(sample_pred_text, pad=False)
# 実行結果
print(predictions)

