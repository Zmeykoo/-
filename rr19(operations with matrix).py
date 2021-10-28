import numpy as np

n, m = 1, 4
A = np.random.randint(10, size=(n, m))
B = np.random.randint(10, size=(n, m))

print(A)
print(B)

def addition(A, B):
    C = np.zeros(shape=(n, m))
    for i in range(n):
        for j in range(m):
            c = A[i][j] + B[i][j]
            C[i][j] = c
    return C
print('Додавання',addition(A,B))

def subtraction(A, B):
    C = np.zeros(shape=(n, m))
    for i in range(n):
        for j in range(m):
            c = A[i][j] - B[i][j]
            C[i][j] = c
    return C
print('Віднімання',subtraction(A,B))


def transpose(A):
    return np.transpose(A)
print('Транспонування\n',transpose(A))

def scalar_multiplication(A, x):
    C = np.zeros(shape=(n, m))
    for i in range(n):
        for j in range(m):
            C[i][j] = x * A[i][j]
    return C
print('Скаляр\n',scalar_multiplication(B,3))


