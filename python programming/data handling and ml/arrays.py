import numpy as np
from numpy.core.fromnumeric import ndim

d1 = [1,2,3,4,5,3]
d2 = [6,7,8,9,0,2]
d3 = [2,3,4,5,2,1]
d4 = [5,2,7,8,1,5]
dic = {1:"A",2:"b",3:"c",4:"d"}

#Function for making array
a1 = np.array([d1,d2])
fro = np.fromiter(dic,dtype = np.int64)
arange = np.arange(1000,1010,1)
linespace = np.linspace(1,10,15)
empty_array = np.empty([3,5])
reshape = linespace.reshape(3,5)
zeroes = np.zeros([3,5],dtype=np.int32,order = "f")
ones = np.ones([3,5])
eye = np.eye(5)
full = np.full([5,5],"ankit")
random_ran = np.random.rand(3,5) 
random_ranint = np.random.randint(1,100,size=(10,9))

#some basic functions
shape = random_ranint.shape
reshape = random_ranint.reshape(9,10)

#accesses elements
new_array = np.array([d1,d2,d3,d4])
hsplit = np.hsplit(new_array,2)
vsplit = np.vsplit(new_array,2)

#concatin arrays
array1 = np.array([d1,d2])
array2 = np.array([d2,d1])
hstack = np.hstack((d1,d2))
vstack = np.vstack((d1,d2))
concate = np.concatenate((array1,array2),axis=0)
concate1 = np.concatenate((array1,array2),axis=1)
#print(array1,"\n********\n",array2)
#print(concate1,"\n********\n",concate)

#attributes
flat = array1.flat
'''for values in flat:
    print(values)'''
print(array2)
print(array2.ndim)
print(array2.nbytes)
print(array2.argmax())
print(array2.argmin())
print(np.where(array2==1))