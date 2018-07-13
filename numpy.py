#1

import numpy as np

a = np.random.random((10,1))
print(a)
m = a.mean()
print("Mean: ", m)

#2

import numpy as np

a = np.random.random((10,1))
print(a)

v = np.var(a)
print("Variance:",v)

s = np.std(a)
print("Standard deviation:",s)


#3

import numpy as np

a = np.random.random((10,20))
print("A",a)

b = np.random.random((20,25))
print("B",b)

m = np.dot(a,b)
print("Multiplication of two matrices:",m)

add = np.sum(m)
print("Addition:",add)

#4

import numpy as np
import math

a = np.array([1,2,3,4,5,6,7,8,9,10])
print(type(a))
print(a.shape)

def f(x):
    return(1/(1+np.exp(-x)))

m = np.array(list(map(f,a)))
print("New array:",m)
