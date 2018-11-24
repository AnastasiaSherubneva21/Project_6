
def derivat(z, i):
    """This function considers the derivative"""
    a = sympy.diff(z, i)
    return(a)

def expression(i1, i2, Px, Py):
    """This function expresses x through y"""
    sympy.expr = (i1 - (Px/Py)*i2)
    c = sympy.solve(sympy.expr, x)
    d = c.count(0.0)
    if d != 0:
        c.remove(0.0)
    e = c.pop()
    e = (e/y)
    return(e)

def budget(I, e, Px, Py):
    """This function calculates the budget"""
    y = I/(Py + e*Px)
    return(y)

import sympy

x = sympy.Symbol('x')
y = sympy.Symbol('y')

Px = float(input('Введите цену фактора x (в ден. ед./шт.):'))
Py = float(input('Введите цену фактора y (в ден. ед./шт.):'))
I = float(input('Введите предполагаемые затраты на факторы производства (в ден. ед.):'))
z = eval(input('Введите производственную функцию от x,y (в ед. продукта):'))

a = derivat(z, x)
b = derivat(z, y)
c = expression(a, b, Px, Py)
d = budget(I, c, Px, Py)
y = round(d, 3)
x = y*c
x = round(x, 3)

print(x, 'ед. фактора x')
print(y, 'ед. фактора y')
