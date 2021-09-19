
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

np.random.uniform(0, 1)
k, m = 0, 0
n = 100
for i in range(0, n):
    x = np.random.uniform(0, 10)
    if x < 5:
        k = k + 1
    else:
        m = m + 1
print(k, m)
