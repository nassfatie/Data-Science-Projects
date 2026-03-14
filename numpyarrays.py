#NumPy stands for numeriCal python. it stores data contigous block of memory.
#it uses less memory than in-built python sequences.
#if is faster than the regular pyhton code.
import numpy as np
data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])
#print(data)
result = data * 10
#print(result)
addition = data + data 
# print(addition)
# print(data.shape)
# print(data.dtype)

#Creating arrays
data1 = [1,2,3,4,5,6] #single array
arr1 = np.array(data1)
# print(arr1)

#nested array
data2 = [[1,4,7,3,6],[5,4,7,2,9]]
arr2 = np.array(data2) #this creates a multidimensional array
# print(arr2)
# print(arr2.ndim)
# print(arr2.shape)
# print(arr2.dtype)

result = np.zeros(10)
# print(result)

result2 = np.ones([2,5])
# print(result2)

x =np.zeros((2,6))
# print(x)

m =np.arange(16)
# print(m)

#indexing and slicing 
#selecting a subset of data or individual elements.
number = np.arange(10)
print(number)
print(number[5])
print(number[5:8])
number[5:8] = 12
print(number)