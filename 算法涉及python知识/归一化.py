import numpy as np

test = np.array([
    [1,1,1],
    [2,2,2],
    [3,3,3]
])

test1 = np.array([
    [1,1,1],
    [2,2,2],
    [3,3,3]
])

# 求比重
def norm1(matrix,type='row'):
    if type == 'row':
        row_sum = matrix.sum(axis=1)
        result = matrix.T/row_sum
        return result.T
    elif type == 'col':
        col_sum = matrix.sum(axis=0)
        #print(col_sum)
        return matrix/col_sum
    else:
        return
    
# 算术平均
def norm2(matrix,type='row'):
    if type == 'row':
        x1 = np.mean(matrix,axis=1)
        print(x1)
        x2 = matrix.T/x1
        return x2.T
    elif type == 'col':
        x1 = np.mean(matrix,axis=0)
        print(x1)
        return matrix/x1
    else:
        return
    
# 几何平均
def norm3(matrix,type='row'):
    if type == 'row':
        x1 = np.sqrt(np.sum(matrix**2,axis=1))
        x2 = matrix.T/x1
        return x2.T
    elif type == 'col':
        x = np.sqrt(np.sum(matrix**2,axis=0))
        return matrix/x
    else:
        return

# Test
if __name__ == '__main__':
    #print(norm1(test,type='col'))
    #print(norm1(test,type='row'))
    m = np.array([3,3,3])
    #print(test/m)
    #print(np.array([x for x in test]))
    # for x in test:
    #     print(x)
    #     print(x/m)
    # print(test.T)

    #print(test*2)
    # m1 = np.array([2,3,4])
    # print(test-m1)
    # print((test.T-m1).T)
    # print(m1.T)
    # print(test-m1.T)
    # print(test-test1)
    # print(norm2(test,type='col'))
    # print(norm2(test,type='row'))
    print(norm3(test,type='col'))
    print(norm3(test,type='row'))