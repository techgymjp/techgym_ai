#Techgym7-1-A

%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

#ステップ関数
def step_function(x):
    return np.where(x<=0, 0, 1)

x = np.linspace(-5, 5)
y = step_function(x)

plt.plot(x, y)
plt.title('Step function')
plt.show()

#シグモイド関数
def sigmoid_function(x):
    return 1/(1+np.exp(-x))

x = np.linspace(-5, 5)
y = sigmoid_function(x)

plt.plot(x, y)
plt.title('Sigmoid function')
plt.show()

#tanh関数
def tanh_function(x):
    return np.tanh(x)

x = np.linspace(-5, 5)
y = tanh_function(x)

plt.plot(x, y)
plt.title('tanh')
plt.show()

#ReLU
def relu_function(x):
    return np.where(x <= 0, 0, x)

x = np.linspace(-5, 5)
y = relu_function(x)

plt.plot(x, y)
plt.title('ReLU')
plt.show()

# leaky RELU
def leaky_relu_function(x):
    return np.where(x <= 0, 0.01*x, x)

x = np.linspace(-5, 5)
plt.title('Leaky ReLU')
y = leaky_relu_function(x)

plt.plot(x, y)
plt.show()

#恒等関数
x = np.linspace(-5, 5)
y = x

plt.plot(x, y)
plt.title('x=y')
plt.show()

#ソフトマックス関数
def softmax_function(x):
    return np.exp(x)/np.sum(np.exp(x)) # ソフトマックス関数

y = softmax_function(np.array([11,12,13]))
print("softmax",y)
