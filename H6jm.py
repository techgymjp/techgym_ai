import numpy as np

def softmax(a):
  c     = np.max(a)
  exp_a = np.exp(a - c)
  sum_exp_a = np.sum(exp_a)
  return exp_a / sum_exp_a

a = np.array([0.5, 3.1, 2.8])
y = softmax(a)
print(y)
