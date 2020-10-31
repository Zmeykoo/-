import numpy as np
#Метод Гауса з вибором головного елемента с. 27
matr = np.array([[-3,4,4,15,-11],
		[7,9,10,0,20],
		[-5,-11,6,-7,-1],
		[16,-6,14,7,20],
		[-6,24,-19,-2,12]])


det = round(np.linalg.det(matr))
print('\n Matrix N=15\n\n',matr,'\n\n\n det =',det)