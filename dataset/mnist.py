import pickle
import gzip
import numpy as np

train_img   = gzip.open("train-images-idx3-ubyte.gz", "rb")
train_label = gzip.open("train-labels-idx1-ubyte.gz", "rb")
test_img    = gzip.open("t10k-images-idx3-ubyte.gz", "rb")
test_label  = gzip.open("t10k-labels-idx1-ubyte.gz", "rb")

img_size = 784

def _load_label(f):
    labels = np.frombuffer(f.read(), np.uint8, offset=8)
    return labels

def _load_img(f):
    data = np.frombuffer(f.read(), np.uint8, offset=16)
    data = data.reshape(-1, img_size)
    return data

def make_pkl():
    dataset = {}
    dataset["train_img"]   = _load_img(train_img)
    dataset["train_label"] = _load_label(train_label)
    dataset["test_img"]    = _load_img(test_img)
    dataset["test_label"]  = _load_label(test_label)

    with open("mnist.pkl", "wb") as f:
        pickle.dump(dataset, f, -1)

make_pkl()
