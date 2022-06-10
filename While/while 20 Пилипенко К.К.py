import random
N = random.randrange(1,100000)
print("N = ",N)
q = N
i = 0
flag = False
while q >= 1:
    i += 1
    r = q % 10
    print(i," - ",r)
    if r == 2:
        flag = True
        break
    q = int(q/10)
print(flag)
        