import numpy as np
from matplotlib import pylab as plt

def sigmoid(x):
  # ここにロジックを記述

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
