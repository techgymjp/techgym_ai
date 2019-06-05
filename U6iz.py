#AI-TECHGYM-N-C2
import numpy as np

#積分をするためのライブラリ
import scipy.integrate as integrate

#積分
def F(x):
    return 2*x*x + 5*x +4
 
result, err = integrate.quad(F, 0, 15)
print('積分結果:{0} 誤差:{1}'.format(result, err))
