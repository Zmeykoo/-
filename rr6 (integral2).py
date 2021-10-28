import numpy as np
from math import sin, cos, pi, log as ln

def f1(x):
    """1+(ln((1)/(1+x))/2*x**2)"""
    return 1+(ln((1)/(1+x))/2*x**2)


def f2(x):
    """sin(x)"""
    return sin(x)

"""метод трапеції"""


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    points = np.zeros((1, int(n) + 1))
    for x in range(points.shape[1]):
        if x == 0:
            points[0][x] = a
        elif x == n:
            points[0][x] = b
        else:
            points[0][x] = points[0][x - 1] + h

    result = (f(points[0][0]) + f(points[0][int(n)])) / 2

    for x in range(1, int(n)):
        result += f(points[0][x])
    return round(h * result, 3)



def main():
    a, b = 0, 1
    c, d = 0, pi/4
    methods = [trapezoidal_rule]
    functions = [f1, f2]
    q1=round(methods[0](functions[0], a, b, 30),4)
    q2=round(methods[0](functions[1], c, d, 30),4)
    Zres = sin(q1+q2)/cos(q1-q2)+3*q2-4*q1
    for i in range(len(methods)):
        print(f"---{i + 1}--------------------------------------------------------------")
        print(f"формула {methods[i].__name__}, функція {functions[0].__doc__}, [{a},{b}] = {q1}")
        print(f"формула {methods[i].__name__}, функція {functions[1].__doc__}, [{c},pi/4] = {q2}")
    print('Z =',round(Zres,4))
main()
