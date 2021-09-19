
import numpy as np
import itertools

for p in itertools.product("23", repeat=4):
    print(''.join(p))

for p in itertools.permutations("567",3):
    print(''.join(str(x) for x in p))
