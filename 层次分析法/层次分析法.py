import numpy as np

def get_weight(matrix):
    """
    层次分析法：获得判断矩阵的权重向量和一致性检验结果CR
    :param matrix: nxn判断矩阵
    :return: 权重向量和CR
    """
    matrix = np.array(matrix,dtype=float)
    n = matrix.shape[0]
    if n != matrix.shape[1]:
        print('not nxn matrix')
        return
    col_sum = matrix.sum(axis=0)
    matrix_1 = matrix/col_sum
    row_sum = matrix_1.sum(axis=1)
    weight = row_sum/row_sum.sum()
    aw = matrix @ weight
    lambda_max = np.mean(aw/weight)
    CI = (lambda_max-n)/(n-1)
    RI_table = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12,
                6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}
    RI = RI_table[n]
    CR = CI/RI
    return weight,CR

matrix1 = np.array([[1,2,3],[2,3,4],[2,4,5],[1,2,1],[2,2,3]])
matrix2 = np.array([[1,2,4,2],[2,3,4,3]])
# n = len(matrix1)
# m = len(matrix2)
# n2 = len(matrix1[0])
# m2 = len(matrix2[0])
# print(n)
# print(m)
# print(n2)
# print(m2)
# print(matrix1.shape)
# print(matrix1.shape[1])
# print(matrix1.sum(axis=0))
# print(matrix1.sum(axis=1))
matrix3 = np.array([[1,1/3,1/4,2],[3,1,1/2,4],[4,2,1,5]
                    ,[1/2,1/4,1/5,1]])
weight,CR = get_weight(matrix3)
get_weight(matrix2)
print(weight,CR)
if CR<0.1:
    print('pass')
else:
    print('not pass')