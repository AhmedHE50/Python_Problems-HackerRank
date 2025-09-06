import numpy as np

n, m = input().split()
n = int(n)
m = int(m)
arr = []

for i in range(n):
    row_data = input().split()
    if len(row_data) == m:
        arr.extend(row_data)

arr = np.array(arr, dtype=np.int64).reshape((n, m))

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(round(np.std(arr), 11))