#Techgym-6-9-A

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
            label='f(x)', color='b')
    ax.plot(xs, [F(x) for x in xs],
            label='F(x)', ls='--', color='b')

    ax.legend()
    plt.show()
    
#######

#正規分布#
def N(mu, sigma):
    x_range = [- np.inf, np.inf]
    def f(x):
        return 1 / (np.sqrt(2 * np.pi) * sigma) *\
                    np.exp(-(x-mu)**2 / (2 * sigma**2))
    return x_range, f

#条件代入
mu, sigma = 2, 0.5
X = N(mu, sigma)

#正規分布
check_prob(X)
plot_prob(X, 0, 4)

#正規分布(scipyでの実装)
rv = stats.norm(2, 0.5)

#各種メソッド
print("期待値と分散",rv.mean(), rv.var())
print("密度関数",rv.pdf(2))
print("分布関数",rv.cdf(1.7))
print("上側100α%点",rv.isf(0.3))
print("確率がαとなる区間",rv.interval(0.9))
print("isfを使用した場合",rv.isf(0.95), rv.isf(0.05))

#グラフ設定
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

#確率分布の確認
xs = np.linspace(-5, 5, 100)
params = [(0, 1), (0, 2), (1, 1)]
for param, ls in zip(params, linestyles):
    mu, sigma = param
    rv = stats.norm(mu, sigma)
    ax.plot(xs, rv.pdf(xs),
            label=f'N({mu}, {sigma**2})', ls=ls, color='b')
ax.legend()
plt.show()

