import numpy as np
import math

def data_add(data):
    if type(data) is np.ndarray:
        data = data.tolist()
    res = []
    for i,k in enumerate(data):
        sum = 0
        for x in range(i+1):
            sum += data[x]
        res.append(sum)
    return np.array(res)

# n = np.array([1,2,3,4,5,6])
# print(data_add(n))

def data_close(data):
    if type(data) is np.ndarray:
        data = data.tolist()
    res = []
    for i,k in enumerate(data):
        if i == 0:
            pass
        else:
            res.append((data[i-1]+data[i])/2)
    return np.array(res)

# n = np.array([1,2,3,4,5,6])
# print(data_close(n))


def build_B(matrix):
    if type(matrix) is not np.ndarray:
        matrix = np.array(matrix)
    matrix = -matrix
    one = np.array([1 for x in matrix])
    res = np.vstack([matrix,one])
    return res.transpose()

# n = np.array([1,2,3,4,5,6])
# print(build_B(n))
# print(n[1:].reshape(-1,1))

def predict(x,a,b,k):
    val0 = (x-(b/a))*math.exp(-a*(k-1))+b/a
    val1 = (x-(b/a))*math.exp(-a*k)+b/a
    return val1 - val0

def gray(matrix0):
    if type(matrix0) is not np.ndarray:
        matrix0 = np.array(matrix0)
    matrix1 = data_add(matrix0)
    matrix_close = data_close(matrix1)
    B = build_B(matrix_close)
    Y = matrix0[1:].reshape(-1,1) #一维矩阵转置
    _u = np.linalg.inv(B.T@B)@B.T@Y
    _a = _u[0].item()
    _b = _u[1].item()
    return predict(matrix0[0],_a,_b,matrix0.size)
    

n = np.array([11,22,31,44,5,62,71,82,93,10,12,14])
print(gray(n))