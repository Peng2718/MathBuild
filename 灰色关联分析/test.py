import numpy as np

m1 = np.array([
    [1,2,3],
    [2,3,4],
    [3,4,5]
])

ma = np.array([
    [1],[2],[3]
])

mb = np.array([
    [1,2,3]
])

print(ma.shape,mb.shape)

m2 = np.array([x*2 for x in m1])
m3 = np.array([x[0]/x[2] for x in m1])
m4 = np.array([x/x[2] for x in m1])
print(m4)
print(m1-mb)
print(np.array([x-mb for x in m1]))
print([x-mb for x in m1])