import numpy as np
import sympy
from math import sqrt, factorial

x = sympy.Symbol('x')
q = sympy.Symbol('q')


def f1(x):
    """x"""
    return x


def f2(x):
    """4x^2"""
    return 4 * (x ** 2)


def f3(x, r=2):
    """sqrt(x^2 + r^2)"""
    if r < 1:
        return 0
    else:
        return sqrt(x ** 2 + r ** 2)


def f4(x, r):
    """sqrt(x^2 + r^2)"""
    return sqrt(x ** 2 + r ** 2)


"""метод прямокутників"""


def rectangle_rule(func, a, b, m):
    h = (b - a) / m
    x = a
    S = func(x)
    for i in range(1, m):
        S += func(x + 0.5 * h + i * h)
    S *= h
    return round(S, 3)


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


"""метод сімпсона(парабол)"""


def Simpson(func, a, b, m):
    h = (b - a) / m
    s = 0.
    try:
        s = func(a) + func(b)
    except ZeroDivisionError:
        pass
    else:
        s = func(b)
    e, n = 0., 0.
    for i in range(0, m):
        if i % 2 == 0:
            try:
                e += func(a + i * h)
            except ZeroDivisionError:
                continue
        else:
            try:
                n += func(a + i * h)
            except ZeroDivisionError:
                continue
    simpson = (h / 3) * (s + 2 * e + 4 * n)
    return round(simpson, 3)


"""кубаторна формула Сімпсона"""


def Cub_Simpson(f, a1, A1, a2, A2, n1, n2):
    h1 = (A1 - a1) / (2 * n1)
    h2 = (A2 - a2) / (2 * n2)
    x_1_0 = a1
    x_2_0 = a2
    s0, s1, s2 = 0, 0, 0
    for i in range(0, n1):
        x_1_i = x_1_0 + (2 * i) * h1
        x_1_1i = x_1_0 + (2 * i + 1) * h1
        x_1_2i = x_1_0 + (2 * i + 2) * h1
        for j in range(0, n2):
            x_2_j = x_2_0 + (2 * j) * h2
            x_2_1j = x_2_0 + (2 * j + 1) * h2
            x_2_2j = x_2_0 + (2 * j + 2) * h2

            s0 += (f(x_1_i, x_2_j) + f(x_1_2i, x_2_j)
                   + f(x_1_2i, x_2_2j) + f(x_1_i, x_2_2j))

            s1 += (f(x_1_1i, x_2_j) + f(x_1_2i, x_2_1j)
                   + f(x_1_1i, x_2_2j) + f(x_1_i, x_2_1j))

            s2 += f(x_1_1i, x_2_1j)

    return round((h1 * h2 * (s0 + 4 * s1 + 16 * s2)) / 9, 3)


"""формула Ньютона-Котеса"""


def cotes_coefficient(i, a, b, n):
    k = ((-1) ** (n - i)) / (factorial(i) * factorial(n - i))
    Q = q
    for j in range(1, n + 1):
        Q *= q - j
    S = sympy.simplify(Q / (q - i))
    integ = sympy.integrate(S, (q, 0, n))
    return (k * integ) / n


def Newton_Cotes(func, a, b, n):
    h = (b - a) / n
    x0 = a
    s = 0
    for i in range(0, n + 1):
        hi = (cotes_coefficient(i, a, b, n))
        xi = x0 + i * h
        f = func(xi)
        s += hi * f
    return round((b - a) * s, 3)


"""метод гауса"""

x = sympy.Symbol('x')
t = sympy.Symbol('t')
A1 = sympy.Symbol('A1')
A2 = sympy.Symbol('A2')
A3 = sympy.Symbol('A3')
gaussian_coefficients = [A1, A2, A3]


def legendre_function(x, i):
    return (((x ** 2) - 1) ** i)


def legendre_polynomial(x, i):
    derivative = sympy.diff(legendre_function(x, i), x, i)
    upper = ((1) / ((2 ** i) * (np.math.factorial(i))))
    return upper * derivative


def equals(x, i):
    if i % 2 == 0:
        return 0
    else:
        return (2 / i)


def gaussian_equations(x, n):
    equations = []
    coefs_used = gaussian_coefficients[:n]
    roots = sympy.solve(sympy.Eq(legendre_polynomial(x, n)))
    for i in range(1, n + 1):
        roots_pow = list(map(lambda x: (x ** (i - 1)), roots))
        eq = sympy.Eq(sum([x * y for x, y in zip(roots_pow, coefs_used)]) - equals(x, i))
        equations.append(eq)
    equations, coefs_used = tuple(equations), tuple(coefs_used)
    result = sympy.solve((equations), (coefs_used))
    return result


def gaussian_quadrature(x, a, b, n, t, f):
    if a == float(-1) and b == float(1):
        h = 1
    else:
        h = (b - a) / 2
    res = 0.
    a_list = list(gaussian_equations(t, n).values())
    t = sympy.solve(sympy.Eq(legendre_polynomial(x, n)))
    for i in range(1, n + 1):
        ai = a_list[i - 1]
        xi = ((b + a) / 2) + (((b - a) / 2) * t[i - 1])
        fi = f(xi)
        res += ai * fi
    return round(h * res, 3)


"""метод чебишова"""

t1 = sympy.Symbol('t1')
t2 = sympy.Symbol('t2')
t3 = sympy.Symbol('t3')
t4 = sympy.Symbol('t4')
t5 = sympy.Symbol('t5')
t6 = sympy.Symbol('t6')
t7 = sympy.Symbol('t7')
t9 = sympy.Symbol('t9')

chebyshev_coefficients = [t1, t2, t3, t4, t5, t6, t7, t9]


def equals1(n, i):
    if i % 2 == 0:
        return (float(n)) / (i + 1)
    else:
        return 0.


def chebyshev_equations(coefs, n, j):
    equations = []
    coefs_used = coefs[:n]
    if n == 8 or n >= 10:
        return "invalid n!"
    else:
        for i in range(1, n + 1):
            eq = sympy.Eq(sum(list(map(lambda x: x ** i, coefs_used))) - equals1(n, i))
            equations.append(eq)
    equations = tuple(equations)
    coefs_used = tuple(coefs_used)
    result = list(sympy.solve((equations), (coefs_used)))
    return float(result[0][j])


def chebyshev_quadrature(f, a, b, n):
    if a == -1. and b == 1.:
        bi = 2. / float(n)
    else:
        bi = (b - a) / float(n)
    res = 0.
    for i in range(1, n + 1):
        ti = chebyshev_equations(chebyshev_coefficients, n, i - 1)
        xi = ((b + a) / 2) + (((b - a) / 2) * ti)
        fi = f(xi)
        res += fi
    return round(bi * res, 3)


def main():
    a, b = map(int, input("Enter a and b (a < b): ").split())
    methods = [rectangle_rule, trapezoidal_rule, Simpson, Newton_Cotes, chebyshev_quadrature]
    functions = [f1, f2, f3]
    for i in range(len(methods)):
        print(f"---{i + 1}--------------------------------------------------------------")
        for j in range(len(functions)):
            print(
                f"формула {methods[i].__name__}, функція {functions[j].__doc__}, [{a},{b}] - {methods[i](functions[j], a, b, 2)}")
    a1, A1, n1 = map(int, input("Enter a1, A1 (a1 < A1) and n1: ").split())
    a2, A2, n2 = map(int, input("Enter a2, A2 (a2 < A2) and n2: ").split())
    print(f"---6--------------------------------------------------------------")
    print(
        f"кубатурна формула Сімпсона, функція {f4.__doc__}, [{a1},{A1}], [{a2},{A2}] - {Cub_Simpson(f4, a1, A1, a2, A2, n1, n2)}")
    print(f"---7--------------------------------------------------------------")
    for j in range(len(functions)):
        print(
            f"формула {gaussian_quadrature.__name__}, функція {functions[j].__doc__}, [{a},{b}] - {gaussian_quadrature(x, a, b, 3, t, functions[j])}")
    print(f"---похибки--------------------------------------------------------------")
    for i in range(len(functions)):
        print(
            f"абсолютна похибка функції {functions[i].__doc__} - {round(abs(trapezoidal_rule(functions[i], a, b, 2) - rectangle_rule(functions[i], a, b, 2)), 3)}")
        print(
            f"відносна похибка функції {functions[i].__doc__} - {round(abs(trapezoidal_rule(functions[i], a, b, 2) - rectangle_rule(functions[i], a, b, 2)) / trapezoidal_rule(functions[i], a, b, 2), 3)}")


main()
