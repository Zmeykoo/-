import numpy as np
matr = np.array([[2,3,4],[9,5,1],[8,9,1]])

Al = np.random.randint(1, size=(3,3))
print(matr)
"""
for y in range(len(matr)):
	for x in range(len(matr)):
		matr[0][x]=0
		print(matr)
print(matr)"""
matr=np.delete(matr, 2, 1)#убирає ряд
print(matr)
matr=np.delete(matr, 0, 0)#убирає с

#Al[x,y] = (round(np.linalg.det(matr)))
print('\n\n',matr,'\n\n',Al)