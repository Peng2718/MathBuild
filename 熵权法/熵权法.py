import numpy as np
import pandas as pd

def entropy_weight(matrix):
    """
    entropy_weight(熵权法)：给多个指标自动算权重，是客观的，
    涉及信息熵计算，信息量打->权重高
    :param matrix: 输入矩阵，横轴是指标，纵轴是方案
    :return weight:权重
    """
    matrix = np.array(matrix,dtype=float)
    n,m = matrix.shape
    x_min = matrix.min(axis=0)
    x_max = matrix.max(axis=0)
    std_matrix = (matrix-x_min)/(x_max-x_min+1e-8)
    std_matrix_sum = std_matrix.sum(axis=0)
    percent_matrix = std_matrix/(std_matrix_sum+1e-8)
    percent_matrix[percent_matrix==0]=1e-8
    k = 1/np.log(n)
    ej = -k*np.sum(percent_matrix*np.log(percent_matrix),axis=0)
    gj = 1-ej
    weight = gj/gj.sum()
    return weight

if __name__ == "__main__":
    # 3学生 3指标：数学 英语 体育
    data = [
        [80, 90, 70],
        [90, 85, 80],
        [70, 80, 90]
    ]
    cols = ["数学", "英语", "体育"]
    
    # 计算
    w = entropy_weight(data)
    
    # 输出
    print("===== 原始数据 =====")
    print(pd.DataFrame(data, columns=cols))
    
    print("\n===== 熵权法结果 =====")
    res = pd.DataFrame({
        "指标": cols,
        "权重w": np.round(w, 4)
    })
    print(res)
    print(f"\n权重总和: {w.sum():.4f}")