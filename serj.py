import numpy as np
import random as rd


def ud(matr):
	"""Searching det 4x4(в розробці)"""
	a=rd.randint(0,len(matr)-1)
	matr = np.delete(matr, a, 0)#убирає row
	matr = np.delete(matr, a, 1)#убирає column
	print(a,'\n', matr)

a = np.array([[2,4,32],[24,5,87],[21,1,0]])
b = np.array([[45,4,3,4],[67,1,7,4],[33,12,21,4],[9,21,1,0]])

ud(b)