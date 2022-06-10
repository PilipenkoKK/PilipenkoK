import numpy as np
import math
def Distance(A,B):
    return math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
x1,x2,x3,y1,y2,y3 = list(np.random.choice(range(-10, 11), 6))
#x1,x2,x3,y1,y2,y3 = [0,3,0,0,0,4]
while (x3-x1)*(y2-y1) == (y3-y1)*(x2-x1):
    x1,x2,x3,y1,y2,y3 = list(np.random.choice(range(-10, 11), 6))    
print("Вершина A (x1, y1): ({0},{1})".format(x1, y1))
 
print("Вершина B (x2, y2): ({0},{1})".format(x2, y2))
print("Вершина C (x3, y3): ({0},{1})".format(x3, y3))
d_AB = Distance([x1,y1],[x2,y2])
print("Длина AB: ", d_AB)
d_AC = Distance([x1,y1],[x3,y3])
print("Длина AC: ", d_AC)
d_BC = Distance([x2,y2],[x3,y3])
print("Длина BC: ", d_BC)
p = (d_AB + d_AC + d_BC)/2
print("Полупериметр: ", p)
S = math.sqrt(p*(p-d_AB)*(p-d_AC)*(p-d_BC))
print("Площадь: ", S)
			