#Tech-Gym-11-9
#グリッドサーチ

# データやモデルを構築するためのライブラリ等のインポート
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

#学習モデル
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

#性能評価
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
