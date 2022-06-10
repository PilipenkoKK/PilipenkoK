import random
N = random.randrange(1,15)
print('N = ', N)
F = 1.0
for i in range(1,N+1):
    F *= i
    print(i," : ", F)
print("Result:",F)
		