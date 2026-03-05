import numpy as np
import pandas as pd

def entropy_weight(data):
    """
    熵权法计算指标权重
    data: 输入矩阵 (样本数, 指标数)
    return: 权重w、标准化矩阵y、信息熵e、差异系数g
    """
    data = np.array(data, dtype=float)
    n, m = data.shape  # n样本 m指标

    # 1. 正向标准化 (0~1)
    x_min = data.min(axis=0)
    x_max = data.max(axis=0)
    y = (data - x_min) / (x_max - x_min + 1e-8)  # 防除0

    # 2. 计算比重 p_ij
    y_sum = y.sum(axis=0)
    p = y / (y_sum + 1e-8)
    p[p == 0] = 1e-8  # 防log(0)

    # 3. 信息熵 e_j
    k = 1 / np.log(n)
    e = -k * np.sum(p * np.log(p), axis=0)

    # 4. 差异系数 g_j
    g = 1 - e

    # 5. 权重 w_j
    w = g / g.sum()

    return w, y, e, g

# ------------------- 测试例子 -------------------
if __name__ == "__main__":
    # 3学生 3指标：数学 英语 体育
    data = [
        [80, 90, 70],
        [90, 85, 80],
        [70, 80, 90]
    ]
    cols = ["数学", "英语", "体育"]
    
    # 计算
    w, y, e, g = entropy_weight(data)
    
    # 输出
    print("===== 原始数据 =====")
    print(pd.DataFrame(data, columns=cols))
    
    print("\n===== 熵权法结果 =====")
    res = pd.DataFrame({
        "指标": cols,
        "信息熵e": np.round(e, 4),
        "差异系数g": np.round(g, 4),
        "权重w": np.round(w, 4)
    })
    print(res)
    print(f"\n权重总和: {w.sum():.4f}")