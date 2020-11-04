#Метод оберненої матриці

import copy as cp
import numpy as np
#вхідні данні та визачник
matr = np.array([[2,-3,1],[2,1,-4],[6,-5,2]])
det = round(np.linalg.det(matr))
B = np.array([2,9,17])
Al = cp.copy(matr)

print('Origin matrix\n',matr,'\n')

def ob(col,raw, matrix):
	"""Пошук мінорів матриці та перетворення їх в алгебраїчні доповнення"""
	Num = matrix[raw][col]
	#видалення рядка і стовпця 
	matrix = np.delete(matrix, raw, 0)#убирає row
	matrix = np.delete(matrix, col, 1)#убирає column
	#пошук визначників
	det0=round(np.linalg.det(matrix))
	#провірка визначників на парність. Парні домножуються на -1
	if (col + raw)%2 != 0:
		det0 *= -1
		print(det0,'- +++++++ парне')
	#зліплення матриці алгебраїчних доповнень
	Al[raw][col]=det0
	print(raw,col,'change. Num =',Num,'\nMatrix =\n',matrix)

for x in range(len(matr)):
	for y in range(len(matr)):
		ob(y,x,matr)
print('Матриця алгебраїчних доповнень\n',Al)
Altr = np.transpose(Al)
print('Транспонована матриця\n',Altr)
Altr = Altr*B
print('Matrix * Vector =\n',Altr)
result=[]
for f in Altr:
	result.append(sum(f)/det)

print('Result =',result)