import numpy as np

n, m = input().split()
n = int(n)
m = int(m)
l = []
for i in range(n):
    row_data = input().split()
    if len(row_data) == m:
        l.extend(row_data)

arr = np.array(l, int).reshape((n, m))
print(arr.transpose())
print(arr.flatten())