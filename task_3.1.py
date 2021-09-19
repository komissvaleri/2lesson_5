
import numpy as np
import itertools
from sympy import *

k, n = 3, 10
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
print(a, b, c, d)
print(x)
print(k, n, k/n)
print("Value of n = {} and k = {}".format(n, k))
nth_bernoulli_poly = bernoulli(n, k)
print("The nth bernoulli polynomial : {}".format(nth_bernoulli_poly))
