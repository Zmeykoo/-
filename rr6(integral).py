import numpy as np
from math import log1p as ln, sin, pi, cos

def final(Q1,Q2):
    Z = sin(Q1 + Q2)/cos(Q1-Q2) + 3*Q2 - 4*Q1
    print ('Z =',round(Z,3))

def Simpson(func, a, b, m):
    """метод сімпсона(парабол)"""
    h = (b-a)/m
    e, n, s = 0., 0., 0.
    try:
        s = func(a) + func(b)
    except ZeroDivisionError:
        pass
    else:
        s = func(b)
    for i in range(0, m):
        if i%2 == 0:
            try:
                e += func(a + i*h)
            except ZeroDivisionError:
                continue
        else:
            try:
                n += func(a + i*h)
            except ZeroDivisionError:
                continue
    simpson = (h/3)*(s + 2*e + 4*n)
    return round(simpson, 3)

def main():
    m = 30
    f1 = lambda x: x*sin(x)/(1-0.7*cos(x)+2*x)
    f3 = lambda x: ln(x)
    a = Simpson(f1,0,pi/2,m)
    b = Simpson(f3,4,7,m)

    print("---метод Сімпсона(парабол)--------------------")
    print(f"функція: x*sin(x)/(1-0.7*cos(x)+2*x), [0,pi/2] = {a}")
    print(f"функція: ln(x), [4,7] = {b}")
    print('------------------------------------------------------')
    final(a, b)
main()
