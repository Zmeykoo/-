import numpy as np
import copy as cp
def oper(matr1,matr2):
	"""Basic operations"""
	do=int(input("Якою операцією бажаєте скористатись?\n1 - додавання\n2 - віднімання\n3 - множення\n\n:"))
	if do == 1:
		print(matr1+matr2)
	elif do == 2:
		print(matr1-matr2)
	elif do == 3:
		result=cp.copy(matr1)
		for x in range(len(matr1)):
			for y in range(len(matr1)):
				a=matr1[x,:]*matr2[:,y]
				result[x,y]=(sum(a))
		print(result)

a = np.array([[2,4,32],[24,5,87],[21,1,0]])
b = np.array([[45,2,3],[67,0,7],[33,21,4]])
print('\nMatrix a\n',a,'\nMatrix b\n',b)
oper(a,b)