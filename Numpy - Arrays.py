import numpy as np

def arrays(arr):
    arr.reverse()
    arr = np.array(arr, float)
    return arr



arr = input().strip().split()
result = arrays(arr)
print(result)