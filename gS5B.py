import tensorflow as tf
from tensorflow       import keras
from tensorflow.keras import datasets, layers, models

import numpy as np
import matplotlib.pyplot as plt

# 手書き文字のデータを読み取り
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

