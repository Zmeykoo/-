from math import fabs,pow
from mpmath import *

n='\n'
for x in range(20):
    mnog = pow(10,x)
    A=3.419911843276937
    a=3.419911843276940
    new=[]
    spi=[A,a]
    for i in spi:
        i*=mnog
        print(i)
        new.append(i)
    print(new)

    b=new[1]-new[0]

    print('* 10^ =',x,n,A,n,a,n,b,'* 10^',x,n)