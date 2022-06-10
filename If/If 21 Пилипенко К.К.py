import random
for i in range(0,5):
    x,y = [random.randrange(-3, 4) for i in range(0,2)]
    print("\nТочка (x,y): ({0},{1})".format(x,y))
    if x == 0 and y == 0:
        print("0. Совпадает с началом координат")
    elif y == 0:
        print("1. Лежит на оси OX")
    elif x == 0:
        print("2. Лежит на оси OY")
    else:
        print("3. Не лежит на координатных осях")
		