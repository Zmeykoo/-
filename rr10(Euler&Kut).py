import numpy as np
from math import sin, pow

def f(x, y):
    return (pow(sin(x-y),2)+pow(sin(2.0*x+3.0*y),2))


def Euler(func, a, b, h):
    '''Метод Ейлера'''
    x0 = a
    y0 = 0
    f0 = func(x0, y0)
    hf0 = h * f0

    x, y, hf, f = [], [], [], []
    x.append(x0)
    y.append(y0)
    f.append(f0)
    hf.append(hf0)
    for i in range(1, 11):
        xi = round(x[i - 1] + h, 4)
        yi = round(y[i - 1] + hf[i - 1], 4)
        fi = round(func(xi, yi), 4)
        hfi = round(h * fi, 4)
        x.append(xi)
        y.append(yi)
        f.append(fi)
        hf.append(hfi)
        if xi == b:
            break
    return x, y, hf, f


'''метод Рунге-Кутта'''


def k1(xi, yi, func):
    return round(func(xi, yi), 3)


def k2(xi, yi, func, h):
    arg1 = ((xi) + (h / 2))
    arg2 = ((yi) + ((h * k1(xi, yi, func)) / 2))
    return round(func(arg1, arg2), 3)


def k3(xi, yi, func, h):
    arg1 = (xi) + ((h / 2))
    arg2 = ((yi) + ((h * k2(xi, yi, func, h)) / 2))
    return round(func(arg1, arg2), 3)


def k4(xi, yi, func, h):
    arg1 = xi + h
    arg2 = ((yi) + (h * k3(xi, yi, func, h)))
    return round(func(arg1, arg2), 3)


def delta_y(xi, yi, func, h):
    coefs = (k1(xi, yi, func)) + (2 * (k2(xi, yi, func, h))) + (2 * (k3(xi, yi, func, h))) + (k4(xi, yi, func, h))
    return round((h / 6) * coefs, 3)


def next_y(xi, yi, func, h):
    return round(yi + delta_y(xi, yi, func, h), 3)


def runge_kutta(a, b, x0, y0, h, func):
    solution_dict = {x0: y0}
    x, y = round(x0, 4), round(y0, 4)
    for i in np.arange(a, b, h):
        y = next_y(x, y, func, h)
        x += round(h, 4)
        print(f'x equals to {round(x, 2)} and y equals to {y}')
        print(f'k1 equals to {k1(x, y, func)}')
        print(f'k2 equals to {k2(x, y, func, h)}')
        print(f'k3 equals to {k3(x, y, func, h)}')
        print(f'k4 equals to {k4(x, y, func, h)}')
        print(f'delta y equals to {(delta_y(x, y, func, h))}')
        solution_dict[round(x, 2)] = y
    return solution_dict


def main():
    x, y, hf, ff = Euler(f, 0, 2, 0.01)
    print("\nМетод Ейлера:")
    print(f"\ti\txi\tyi\tfi")
    for i in range(0, 11):
        print(f"\t{i}\t{x[i]}\t{y[i]}\t{ff[i]}")
    print("\nМетод Рунге-Кутта:")
    print(runge_kutta(0., 2., 0., 3., 0.01, f))
main()
