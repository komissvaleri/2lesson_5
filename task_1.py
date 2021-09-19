
import numpy as np

np.random.uniform(0, 1)
for i in range(0, 10):
    x = np.random.uniform(0, 50)
    if x <= 18:
        print('red')
    elif 19 < x < 36:
        print('black')
    else:
        print('zero')
