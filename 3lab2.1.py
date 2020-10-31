#другий рівень(Крамер)
import numpy as np
import copy as cp

n, m = map(int, input("Enter size, please:").split(','))

A = np.random.randint(10, size=(n,m))
B = np.random.randint(10, size=(n,1))
det = round(np.linalg.det(A))
res=[]

print('Matrix',n,'x',m,'\n',A,'\nVector\n', B)
print("НАШ ВИЗНАЧНИК =",det)

def vyzn(var, matrix):
	"""Kramer Go"""
	matrix[:,x]=B[:,0]
	res.append(round(np.linalg.det(matrix))/det)
	print(var, '\n Matrix\n',matrix, round(np.linalg.det(matrix)))


if det==0:
	print('Визначник = 0, тому СЛАР не розв*язується ')
else:
	for x in range(len(A)):
		vyzn(x,cp.copy(A))

print('Result =',res)