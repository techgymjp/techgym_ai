import pickle
import numpy as np
import tensorflow as tf
from matplotlib import pylab as plt

dataset_file = open("./dataset/mnist.pkl", "rb")

# pklデータのload
def load_data(dataset_file, flatten=True):
  dataset = pickle.load(dataset_file)

  if not flatten:
    dataset["train_img"] = dataset["train_img"].reshape(-1, 28, 28)
    dataset["test_img"]  = dataset["test_img"].reshape(-1, 28, 28)

  return (dataset["train_img"], dataset["train_label"]), (dataset["test_img"], dataset["test_label"])

(train_img, train_label),(test_img, test_label) = load_data(dataset_file, flatten=False) 
train_img, test_img = train_img.astype(np.float32) / 255.0, test_img.astype(np.float32) / 255.0
