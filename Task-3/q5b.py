## Array Data Type conversion
import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(arr.dtype)

arr = np.array(arr,dtype="float32")
print(arr)
print(arr.dtype)

arr = np.array(arr,dtype="int8")
print(arr)
print(arr.dtype)

arr = np.array(arr,dtype="int64")
print(arr)
print(arr.dtype)

arr = np.array(arr,dtype="float64")
print(arr)
print(arr.dtype)
