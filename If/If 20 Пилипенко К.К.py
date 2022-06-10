import random
A,B,C = random.sample(range(-10, 10), 3)
print("Число A:", A)
print("Число B:", B)
print("Число C:", C)
AB = abs(A-B)
AC = abs(A-C)
print("Расстояние от A до B:",AB)
print("Расстояние от A до C:",AC)
if AB < AC:
    print("В ближе к A")
elif AB > AC:
    print("C ближе к A")
else:
    print("B и C равноудалены от A")
					