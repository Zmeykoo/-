from math import pow as p, fabs as fb
from mpmath import *
n='\n'
def fun(x1,x2,x3):
    """Main func"""
    return (x1+p(x2,2))/x3
    
def short(A):
    """zaokrugl"""
    return round(A,14)


def measers(A,a):
    """Пошук абсолютної та відносної похиби"""
    aBs=fb(a-A)
    print(aBs)
    
A=fun(3.15,0.831,1.123)
a=short(A)
measers(A,a)
print(' a =',a,'\n','A =',A,n)