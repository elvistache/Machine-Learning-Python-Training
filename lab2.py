import numpy as np
a = np.array([(12,23,38,65),(32,22,12,44),(33,12,67,11)])
b = np.array([(11,12,13),(20,21,22),(30,31,32),(40,41,42)])
c = np.array([(1,2,3),(3,2,1),(4,5,6)])

ex1 = np.transpose(a) + b
print(ex1)
ex2 = np.transpose(b) + a
print(ex2)
ex3 = a - np.transpose(b)
print(ex3)
ex4 = 5 * (np.transpose(a))
print(ex4)
i = [(1,0,0),(0,1,0),(0,0,1)]
                
print(np.linalg.inv(c))
