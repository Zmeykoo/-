a, b = -1, 1
epsilon = 0.001

def f(x3):
    return x3**3-3*x3**2+12*x3-12

def df_dx(x2):
    return 3*x2**2-6*x2+12

def df_dx2(x4):
    return 6*x4-6

def h1(i):
    return round(a + i*(b-a)/3, 4)

def h2(i):
    return round(a + (i+1)*(b-a)/3, 4)

def newton_method():
    lst = []

    for i in range(1):
        a0 = h1(i)
        b0 = h2(i)
        if f(a0)*df_dx2(a0) > 0:
            x0 = a0
        else:
            x0 = b0
        xp = x0
        bl = True
        while bl:
            xn = round(xp - (f(xp)/df_dx(xp)), 3)
            res = xn - xp
            xp = xn
            if abs(res) <= epsilon:
                lst.append(xp)
                print(f"x{i} = {xp}")
                bl = False
    return lst

newton_method()
