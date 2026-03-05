import numpy as np

def topsis(matrix):
    """
    topsis法：通过靠近最优解，远离最劣解的，
    计算每个方案与其的距离来进行评价
    :param matrix: 输入矩阵，横坐标是评价准则，
    纵坐标是方案
    :return score:方案的得分
    """
    # 获得
    matrix = np.array(matrix,dtype=float)
    col_norm = np.sqrt(np.sum(matrix**2,axis=0))
    matrix_1 = matrix/col_norm
    best = np.max(matrix_1,axis=0)
    worst = np.min(matrix_1,axis=0)
    d_best = np.sqrt(np.sum((matrix_1-best)**2,axis=1))
    d_worst = np.sqrt(np.sum((matrix_1-worst)**2,axis=1))
    score = (d_worst)/(d_worst+d_best)
    return score

test_matrix = [
    [80,90,70],
    [90,85,80],
    [70,80,90]
]

print(topsis(test_matrix))