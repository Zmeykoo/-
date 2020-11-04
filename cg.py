
import copy as cp
import numpy as np
matr = np.array([[2,-3,1],[2,1,-4],[6,-5,2]])
det = round(np.linalg.det(matr))
B = np.array([2,9,17])
Al = cp.copy(matr)
print('Origin matrix\n',matr,'\n')
def ob(col,raw, matrix):
	"""Метод обереної матриці"""
	Num = matrix[raw][col]
	matrix = np.delete(matrix, raw, 0)#убирає row
	matrix = np.delete(matrix, col, 1)#убирає column
	
	det0=round(np.linalg.det(matrix))
	if (col + raw)%2 != 0:
		det0 *= -1
		print(det0,'- +++++++ парне')
	Al[raw][col]=det0
	print(raw,col,'change. Num =',Num,'\nMatrix =\n',matrix)

for x in range(len(matr)):
	for y in range(len(matr)):
		ob(y,x,matr)
print('Матриця алгебраїчних доповнень\n',Al)
tran = np.transpose(Al)
print('Транспонована матриця\n',tran)
tryres = tran*B
print('X =\n',tryres)
result=[]
for f in tryres:
	result.append(sum(f)/det)

print('Result =',result)