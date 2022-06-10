import random
import math
N = random.randrange(1,15)
N = 20
print('N = ', N)
F = 1.0
S = 1.0
for i in range(1,N+1):
    F /= i
    S += F
    print(i," : ", F," : ", S)
print("Result:",S)
print("e = ",math.exp(1))
				