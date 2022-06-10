import random
import math
x1,x2 = random.sample(range(-10, 10), 2)
y1,y2 = random.sample(range(-10, 10), 2)
print("Точка 1 (x1, y1): ({0},{1})".format(x1, y1))
print("Точка 2 (x2, y2): ({0},{1})".format(x2, y2))
side1 = abs(x1 - x2)
side2 = abs(y1 - y2)
print("Сторона 1: ", side1)
print("Сторона 2: ", side2)
d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print("Расстояние: ", d)
				