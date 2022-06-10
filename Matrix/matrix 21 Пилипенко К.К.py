import random
import numpy
#M = random.randrange(2,10)
M = 6
print("M = ",M)
a = numpy.zeros((M, M))
#a.astype(int)
k = 0
for i in range(M):
    for j in range(M-i):
        k += 1
        a[j][i] = k
    k += M-i-1
k = M+1
for j in range(1,M):
    for i in range(j,M):
        a[M-j][i] = k
        k += 1
    k += M-j
print(a)
for i in range(M):
    for j in range(M-i):
        print(a[j][i], end=" ")
    for j in range(i+1,M):
        print(a[M-i-1][j], end=" ")
						