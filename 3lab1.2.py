import numpy as np
import copy as cp
import random as rd


def determ(matr):
	"""Searching det"""
	det=0
	def three(matr):
		"""Пошук визначника 3x3"""
		det = matr[0,0]*matr[1,1]*matr[2,2]+matr[0,1]*matr[1,2]*matr[2,0]+matr[0,2]*matr[1,0]*matr[2,1]-matr[0,2]*matr[1,1]*matr[2,0]-matr[0,0]*matr[1,2]*matr[2,1]-matr[0,1]*matr[1,0]*matr[2,2]
		print('det =',det)
	
	print('Matrix\n',matr)


	print('det =',round(np.linalg.det(matr))) #easy method
	
	if len(matr) == 1:
		det = mat[0,0]
	elif len(matr) == 2:
		print('byt')#det = matr[0,0]*matr[1,1]-matr[0,1]*matr[1,0]
	elif len(matr) == 3:
		three(matr)
	elif len(matr) == 4:
		ud(b)



b = np.array([[2,4,32],[24,5,87],[21,1,0]])
a = np.array([[45,4,3,4],[67,1,7,4],[33,12,21,4],[9,21,1,0]])
c = np.array([[1,2],[2,1]])

determ(b)

