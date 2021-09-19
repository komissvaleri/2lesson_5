
import numpy as np
import matplotlib.pyplot as plt

mu = 100
sigma = 15
x = mu + sigma * np.random.randn(1000)
plt.hist(x, bins=9, facecolor="blue", alpha=0.5)

plt.show()
