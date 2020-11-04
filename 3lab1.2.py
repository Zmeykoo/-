import numpy as np
import copy as cp

det=0
def determ(matr,det):
	"""Searching det"""
	def three(minmatr):
		"""Пошук визначника 3x3"""
		det = matr[0,0]*matr[1,1]*matr[2,2]+matr[0,1]*matr[1,2]*matr[2,0]+matr[0,2]*matr[1,0]*matr[2,1]-matr[0,2]*matr[1,1]*matr[2,0]-matr[0,0]*matr[1,2]*matr[2,1]-matr[0,1]*matr[1,0]*matr[2,2]
		print(det)
	print('Matrix\n',matr)
	print('det =',round(np.linalg.det(matr))) #easy method

	if len(matr) == 1:
		det = mat[0,0]
	elif len(matr) == 2:
		print('byt')#det = matr[0,0]*matr[1,1]-matr[0,1]*matr[1,0]
	elif len(matr) == 3:
		three(matr)
		print ('det =',det)
	elif len(matr) >= 4:
		
		
		print('')
	else:
		print('Здається твоя матриця неквадратна, друже...')


a = np.array([[2,4,32],[24,5,87],[21,1,0]])
b = np.array([[45,2,3],[67,0,7],[33,21,4]])
c = np.array([[1,2],[2,1]])

print(len(c[:,:]),'\n')
determ(b,det)

