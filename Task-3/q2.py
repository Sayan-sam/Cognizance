import numpy as np

## Initializing two arrays
arr1 = np.array([1,0,0,0,1,0])
arr2 = np.array([0,0,1,1,0,1])

print("First Array:")
print(arr1)
print("Second Array:")
print(arr2)
print(np.array_equal(arr1,arr2))