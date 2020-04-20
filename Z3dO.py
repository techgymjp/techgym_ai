#Techgym-6-8-A

#インポート
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline
import japanize_matplotlib

from scipy import stats

# グラフの線の種類
linestyles = ['-', '--', ':']

def E(X, g=lambda x: x):
    x_set, f = X
    return np.sum([g(x_k) * f(x_k) for x_k in x_set])

def V(X, g=lambda x: x):
    x_set, f = X
    mean = E(X, g)
    return np.sum([(g(x_k)-mean)**2 * f(x_k) for x_k in x_set])

def check_prob(X):
    x_set, f = X
    prob = np.array([f(x_k) for x_k in x_set])
    assert np.all(prob >= 0), '負の確率があります'
    prob_sum = np.round(np.sum(prob), 6)
    assert prob_sum == 1, f'確率の和が{prob_sum}になりました'
    print(f'期待値は{E(X):.4}')
    print(f'分散は{(V(X)):.4}')

def plot_prob(X):
    x_set, f = X
    prob = np.array([f(x_k) for x_k in x_set])
    
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.bar(x_set, prob, label='prob')
    ax.vlines(E(X), 0, 1, label='mean')
    ax.set_xticks(np.append(x_set, E(X)))
    ax.set_ylim(0, prob.max()*1.2)
    ax.legend()
    
    plt.show()

#######

#ベルヌーイ分布
def Bern(p):
    x_set =
    def f(x):
    
    return x_set, f

#条件
p =
X =

#ベルヌーイ分布
check_prob()
plot_prob()

#ベルヌーイ分布(scipyでの実装)
rv =

print("確率関数")
print("累積密度関数")


#ポアソン分布
from scipy.special import factorial

def Poi(lam):
    x_set =
    def f(x):

    return x_set, f

#λ=3のとき
lam =
X =

#ポアソン分布
check_prob()
plot_prob()


#グラフ設定
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

#ポアソン分布(scipyでの実装)
x_set = np.arange(20)
for lam, ls in zip([3,8,15], linestyles):
    rv =
    ax.plot(x_set, ,
            label=f'lam:{lam}', ls=ls, color='b')
ax.set_xticks(x_set)
ax.legend()
plt.show()

