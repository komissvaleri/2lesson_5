
import numpy as np
import itertools

for p in itertools.product("123", repeat=3):
    print(''.join(p))
