import random
N = random.randint(10,20)
L = random.randrange(0,N)
K = random.randint(0,L)
#N = 10
print("N = ", N)
print("L = ", L)
print("K = ", K)
A = [random.randrange(1,20) for i in range(N)]
print("Initial:")
print(A)
s = 0
for i in range(K,L+1):
    s += A[i]
    print(i,":",A[i])
print("Sum = ",s)
print()
print(A[K:L+1])
print("Sum = ",sum(A[K:L+1]))
				