import random
#N = random.randint(10,25)
N = 10
print("N = ", N)
A = [random.randrange(1,20) for i in range(N)]
print("Initial:")
print(A)
k = -1
for i in range(1,N-1):
    if A[0] < A[i] and A[i] < A[N-1]:
        print(i,A[i])
        k = i
print(k)
		