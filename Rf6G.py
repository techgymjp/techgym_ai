#tech-gym-13-3-Q
#センサーデータ分析

#必要なものをインポートする
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.model_selection import train_test_split
import sklearn.svm

# 四国電力の電力消費量データを読み込み


#気象データを読み込み

# 「時」の列は使わないので、削除

# 列の名前を英語に変更

#欠損値を-1にする

# 月, 日, 時の取得

# 気象データと電力消費量データをいったん統合して時間軸を合わせたうえで、再度分割


# 学習と性能の評価

# 出力
