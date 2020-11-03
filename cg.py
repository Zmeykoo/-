import numpy as np
matr = np.array([[2,3,4],[9,5,1],[8,9,1],[2,0,1],[5,6,7]])

A = np.random.randint(10, size=(5,5))
Al = np.random.randint(1, size=(5,5))
print(A,'\n')
def ob():
	"""Метод обереної матриці"""
	



for x in range(len(A)):
	A=np.delete(A, x, 1)#убирає column
	A=np.delete(A, x, 0)#убирає row
	print(A)
#Al[x,y] = (round(np.linalg.det(matr)))
