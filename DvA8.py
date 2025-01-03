#Techgym-6-10-A

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, integrate
from scipy.optimize import minimize_scalar

%precision 3
%matplotlib inline

linestyles = ['-', '--', ':']

def E(X, g=lambda x: x):
    x_range, f = X
    def integrand(x):
        return g(x) * f(x)
    return integrate.quad(integrand, -np.inf, np.inf)[0]

def V(X, g=lambda x: x):
    x_range, f = X
    mean = E(X, g)
    def integrand(x):
        return (g(x) - mean) ** 2 * f(x)
    return integrate.quad(integrand, -np.inf, np.inf)[0]

def check_prob(X):
    x_range, f = X
    f_min = minimize_scalar(f).fun
    assert f_min >= 0, '密度関数が負の値をとります'
    prob_sum = np.round(integrate.quad(f, -np.inf, np.inf)[0], 6)
    assert prob_sum == 1, f'確率の和が{prob_sum}になりました'
    print(f'期待値は{E(X):.3f}')
    print(f'分散は{V(X):.3f}')
    
def plot_prob(X, x_min, x_max):
    x_range, f = X
    def F(x):
        return integrate.quad(f, -np.inf, x)[0]

    xs = np.linspace(x_min, x_max, 100)

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.plot(xs, [f(x) for x in xs],
            label='f(x)', color='gray')
    ax.plot(xs, [F(x) for x in xs],
            label='F(x)', ls='--', color='gray')

    ax.legend()
    plt.show()
    
#######

#カイ二乗分布#

n =
rv =
sample_size =
# 標準正規分布から10×100万のサイズで無作為抽出
Zs_sample =
# axis=0の方向で総和をとり、標準正規分布の二乗和の標本データを得る
chi2_sample =

#グラフ設定
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

#確率分布とヒストグラム
rv_true =
xs = np.linspace(0, 30, 100)
ax.hist(, bins=100, density=True,
        alpha=0.5, label='chi2_sample')
ax.plot(xs, rv_true.pdf(xs), label=f'chi2({n})', color='gray')
ax.legend()
ax.set_xlim(0, 30)
plt.show()

#グラフ設定
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

#確率分布の確認
xs = np.linspace(0, 20, 500)
for n, ls in zip([3, 5, 10], linestyles):
    rv =
    ax.plot(xs, ,
            label=f'chi2({n})', ls=ls, color='gray')
    
ax.legend()
plt.show()

#上側100α%点
rv =
print("上側100α%点")


