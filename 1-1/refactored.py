import math

def calcMaxSize(comparison, increment):
    n = 1
    while comparison(n) * 10**(-6) <= 1:
        n += increment
        print(comparison(n) * 10**(-6))
    return n

def factorial(n):
    return math.factorial(n)
def two_njou(n):
	return 2**n
def n_cubed(n):
	return n**3
def n_squared(n):
	return n**2
def n_lgn(n):
	return n * math.log2(n)
def root_n(n):
	return math.sqrt(n)


print("MAX SIZE:", calcMaxSize(n_lgn, 1) - 1)
# グラフ描画
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 100000, 1)
y = x * np.log2(x)
plt.plot(x, y)
plt.show()




