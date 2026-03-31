import numpy as np
import math
# a = []
# for i in range(20):
#     a.append(i+1)
# n1 = np.array(a)
# print(n1)

# n2 = np.zeros((4,5))
# print(n2)

# n3 = np.eye(5)
# print(n3)

# n4 = np.arange(0,10,2)
# print(n4)

# arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
# new = arr.reshape((1,9))
# print(new)
# print(arr[1])
# print(arr[:,2])
# print(arr[:1,:2])
# print(arr[:2,:2])
# print(arr[arr>5])

# A = np.array([[1,2],[3,4]])
# B = np.array([[2,3],[3,4]])
# print(A+B)
# print(A-B)
# print(A*B)
# print(A@B)
# A2 = np.array([math.sqrt(x) for y in A for x in y],dtype=float)
# print(A2)

n = np.array([1,2,3,4,5,6])
nl = n.tolist()
res = []
for i,k in enumerate(nl):
    if i == 0:
        pass
    else:
        res.append((nl[i-1]+nl[i])/2)