import numpy as np

n = int(input())
arr = []

for i in range(n):
    row_data = input().split()
    if len(row_data) == n:
        arr.extend(row_data)

arr = np.array(arr, float).reshape((n, n))
print(round(np.linalg.det(arr), 2))