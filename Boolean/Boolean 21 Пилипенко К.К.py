import random
N = random.randrange(100,1000)
print("Число: ", N)
d2 = int(N/100)
d1 = int((N-d2*100)/10)
d0 = N%10
print("Сотни: ", d2)
print("Десятки: ", d1)
print("Единицы: ", d0)
x = (d2 < d1) and (d1 < d0)
print("Цифры образуют возрастающую последовательность: ", x)
								