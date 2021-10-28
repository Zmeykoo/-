from math import sin

y = []
def routs():
    n = 0
    i = -3.0
    x = round(i, 3)
    bl = True
    while bl:
        if x >= 3.0:
            bl = False
        if round(sin(x), 2) - round(x**3, 2) == 0:
            n += 1
            y.append(round(x, 3))
        x += 0.01
    return n

print(f'Корінці = {routs()}')
print(f"x = {y}")
