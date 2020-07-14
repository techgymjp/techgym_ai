#techgym-10-11-Q

import os
import cv2
import json
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline

#エラー回避のための記述
import tensorflow as tf
tf.to_float = lambda x: tf.cast(x, tf.float32)
tf.to_int32 = lambda x: tf.cast(x, tf.int32)

from ssd import SSD

#SSDトレーニング
#モデルの名前を指定する. ここではSSD7を指定する.
#学習を行うには学習モードにするため, ``mode``に'training'を渡す

model_name = 'ssd_7'
ssd = SSD(model_name, mode='training')

#モデル構造を表示
#ssd.model.summary()

#画像データが格納されているディレクトリと対応する学習用データと検証用データに対するメタデータを指定する.
train_images_dir = os.path.join('train_data', 'train_images')
val_images_dir = os.path.join('train_data', 'train_images')
train_annotation_path = os.path.join('train_data', 'train_annotations.json')
val_annotation_path = os.path.join('train_data', 'val_annotations.json')

#学習用と検証用でデータ生成器を``set_generator``メソッドで作成する.
#あらかじめ``batch_size``を決めておく. ここでは16にしておく.

batch_size =16
ssd.set_generator(train_images_dir, train_annotation_path, batch_size, val_images_dir, val_annotation_path)


#設定
epochs = 10

#まず``ModelCheckpoint``モジュールで``model_checkpoint``オブジェクトを作成する.
#これはepochごとにモデルを保存するモジュールである.
#``filepath``でパス名を指定する.
#今回の場合はsaved_modelsディレクトリ以下にモデルが保存される形とする.
#``monitor``でモニターする値(検証時のaccuracyやloss)を指定する.
#今回は検証時の損失'val_loss'とする.
#``save_best_only``は, Trueにするとモニターする値において
#現状で1番よい結果を出した場合のみモデルが保存される.

from keras.callbacks import ModelCheckpoint

save_dir = os.path.join(os.getcwd(), 'my_trained_models')
model_name = 'ssd7_epoch-{epoch:02d}.h5'
if not os.path.isdir(save_dir):
    os.makedirs(save_dir)
filepath = os.path.join(save_dir, model_name)
model_checkpoint = ModelCheckpoint(filepath=filepath,
                                   monitor='val_loss',
                                   verbose=1,
                                   save_best_only=True,
                                   save_weights_only=True,
                                   mode='auto',
                                   period=1)

#
#次に``EarlyStopping``モジュールで``earlystopper``オブジェクトを作成する.
#こちらで決めた基準を満たさない場合は学習を打ち切るモジュールである.
#``monitor``でモニターする値(検証時のaccuracyやloss)を指定する.
#今回は検証時の損失関数'val_loss'とする.
#``min_delta``でモニターする値について改善したと判定される最小変化値を指定する. ここでは0.
#``patience``でモニターする値について改善がみられるまで待つepoch数を指定する.
#つまり, ここで指定した数のepoch数が過ぎても改善がみられなければ学習を打ち切る. ここでは3とする.

from keras.callbacks import EarlyStopping

earlystopper = EarlyStopping(monitor='val_loss', min_delta=0, patience=3)


#次に``LearningRateScheduler``モジュールで``lr_scheduler``オブジェクトを作成する.
#これは各epochごとに呼び出され, 学習率を減衰させるモジュールである.
#epochを渡してその時の学習率を返す関数(``lr_schedule``)を定義して,
#``LearningRateScheduler``に渡すことで作成する.
#ここでは初期値0.001に対して, 50epoch以降は0.0005にする.

from keras.callbacks import LearningRateScheduler

def lr_schedule(epoch):
    lr = 0.001
    
    if epoch >= 50:
        lr *= 0.5
    
    return lr

lr_scheduler = LearningRateScheduler(lr_schedule, verbose=1)

#epochごとの損失をcsvファイルとして保存するために``CSVLogger``モジュールで
#``csv_logger``オブジェクトを作成する.

from keras.callbacks import CSVLogger

csv_logger = CSVLogger(filename='ssd7_training_log.csv',
                       separator=',',
                       append=True)

#以上4つのオブジェクトを``list``として保存する.
callbacks = [model_checkpoint,
             csv_logger,
             lr_scheduler,
             earlystopper]

#最適化手法を定義し, ``optimizer``に渡す.
from keras.optimizers import Adam

optimizer = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)

#バージョン違いの吸収
tf.log = lambda x: tf.math.log(x)

#実行するときはコメントをはずす(実行するにかなり時間がかかる)
#ssd.train(epochs, optimizer, callbacks)

