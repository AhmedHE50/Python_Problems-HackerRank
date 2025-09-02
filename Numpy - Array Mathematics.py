import numpy as np

n, m = input().split()
n = int(n)
m = int(m)
l1 = []
l2 = []

# accept the dimensions of the matrix and then take the numbers of each matrix using two loops.

for i in range(n):
    row_data = input().split()
    if len(row_data) == m:
        l1.extend(row_data)

l1 = np.array(l1, int).reshape((n, m))

for i in range(n):
    row_data = input().split()
    if len(row_data) == m:
        l2.extend(row_data)

l2 = np.array(l2, int).reshape((n, m))

print(l1 + l2)
print(l1 - l2)
print(l1 * l2)
print(l1 // l2)
print(l1 % l2)
print(l1 ** l2)
