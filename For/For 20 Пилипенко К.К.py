import random
N = random.randrange(1,10)
print('N = ', N)
F = 1.0
S = 0.0
for i in range(1,N+1):
    F *= i
    S += F
    print(i," : ", F," : ", S)
print("Result:",S)
				