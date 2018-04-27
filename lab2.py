import numpy as np
a = np.array([(12,23,38,65),(32,22,12,44),(33,12,67,11)])
b = np.array([(11,12,13),(20,21,22),(30,31,32),(40,41,42)])
c = np.array([(1,2,3),(3,2,1),(4,5,6)])

def solve(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        total = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            total += mul * solve(m, sign * matrix[0][i])
    return total

try:
    ex1 = np.transpose(a) + b
    print(ex1)
    ex2 = np.transpose(b) + a
    print(ex2)
    ex3 = a - np.transpose(b)
    print(ex3)
    ex4 = 5 * (np.transpose(a))
    print(ex4)
    i = [(1,0,0),(0,1,0),(0,0,1)]

    #ex5
    if solve(c,1)==0:
        raise ValueError("Matrice Singulara! /n Nu se poate calcula inversa")
    print(np.linalg.inv(c))
except:
    print("o eroare")
finally:
    print("Calcule facute")

