import numpy as np
import copy

n, m = 4, 4

A = np.array([[-5,1,-7,8],[0,9,-3,-4],[-3,7,5,0],[0,-7,-11,-4]])
B = np.array([[33],[-6],[-13],[10]])
print('A\n',A)
print('B\n',B)

def minor(A, row_index, col_index):
    C = np.zeros(shape=A.shape)
    for i in range(A.shape[0]):
        if i == row_index:
            continue
        else:
            for j in range(A.shape[1]):
                if j == col_index:
                    continue
                else:
                    C[i][j] = A[i][j]
    C = np.delete(C, row_index, 0)
    C = np.delete(C, col_index, 1)
    return C

def transpose(A):
    C = np.zeros(shape=(n, m))
    for i in range(n):
        for j in range(m):
            C[i][j] = A[j][i]
    return C

def cofactors(A):
    if A.shape == (2, 2):
        return A[0][0] * A[1][1] - A[1][0] * A[0][1]
    s = 0
    for i in range(A.shape[1]):
        s += A[0][i] * (-1) ** (i + 2) * cofactors(minor(A, 0, i))
    return s

def determinant(A):
    res = 0
    res += cofactors(A)
    return res
print('Визначник =',determinant(A))

def reverse_matrix(A):
    det = determinant(A)
    cofactors_matrix = np.zeros(shape=(n, m))
    reversed_matrix = np.zeros(shape=(n, m))
    if det == 0:
        print("матриця вироджена")
        return None
    else:
        for i in range(n):
            for j in range(m):
                C = minor(A, i, j)
                cofactor = cofactors(C)
                cofactors_matrix[i][j] = cofactor
    for i in range(n):
        for j in range(m):
            if ((i + 1) + (j + 1)) % 2 == 0:
                pass
            else:
                cofactors_matrix[i][j] = -cofactors_matrix[i][j]
    cofactors_matrix = transpose(cofactors_matrix)
    for i in range(n):
        for j in range(m):
            reversed_matrix[i][j] = cofactors_matrix[i][j] / det
    return reversed_matrix

def multiplication(A, B):
    c_rows, c_columns = A.shape[0], B.shape[1]
    C = np.zeros(shape=(c_rows, c_columns))
    for i in range(c_rows):
        for j in range(c_columns):
            c = 0
            for k in range(B.shape[0]):
                c += A[i][k] * B[k][j]
            C[i][j] = c
    return C

def matrix_method(A, B):
    A_reversed = reverse_matrix(A)
    X = multiplication(A_reversed, B)
    return X
print(matrix_method(A,B))

# cramer method version one
def det_i(A, B, i):
    D = copy.deepcopy(A)
    for j in range(n):
        D[j][i] = B[j]
    return D

def cramer_method(A, B):
    X = np.zeros(shape=(n, 1))
    det = determinant(A)
    for i in range(n):
        delta_matrix = det_i(A, B, i)
        delta_matrix_det = determinant(delta_matrix)
        x = delta_matrix_det / det
        X[i][0] = x
    return X
print(cramer_method(A,B))

# cramer method version two
def cramera_matrix(A, B, det, i):
    for y in range(A.shape[0]):
        A[y][i - 1], B[y] = B[y], A[y][i - 1]
    d = determinant(A)
    x = d / det
    for y in range(A.shape[0]):
        A[y][i - 1], B[y] = B[y], A[y][i - 1]
    return x

def cramera(A, B):
    X = np.zeros(shape=B.shape)
    for i in range(A.shape[1]):
        X[i][0] = cramera_matrix(A, B, determinant(A), i + 1)
    return X
