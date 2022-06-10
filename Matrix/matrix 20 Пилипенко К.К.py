import random
import numpy as np
M = random.randrange(2,7)
N = random.randrange(2,7)
K = random.randrange(0,N)
print("M = ",M,"; N = ",N)
a = np.zeros((M, N))
for i in range(M):
    for j in range(N):
        a[i][j] = random.randrange(1,5)
print(a)
b = a.prod(0)
print(b)
		