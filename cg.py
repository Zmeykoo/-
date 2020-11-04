
import copy as cp
import numpy as np
matr = np.array([[1,2,1],[3,4,1],[7,2,5]])
n, m = 5, 5
A = np.random.randint(10, size=(n,m))
Al = np.random.randint(1, size=(n,m))
print('Origin matrix\n',matr,'\n')
def ob(col,raw, matrix):
	"""Метод обереної матриці"""
	Num=matrix[raw][col]
	matrix=np.delete(matrix, raw, 0)#убирає row
	matrix=np.delete(matrix, col, 1)#убирає column
	
	det0=round(np.linalg.det(matrix))
	Al[raw][col]=det0
	print(raw,col,'change. Num =',Num,'\nMatrix =\n',matrix)



for x in range(len(matr)):
	for y in range(len(matr)):
		ob(y,x,matr)
print(Al)
