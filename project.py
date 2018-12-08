
def diff_or_min(z1):
    """This function determines whether a function is a minimum"""

    mi = z1.find('min')
    if mi != -1:
        return(1)
    else:
        return(0)

def type_diff_f(a, b):
    """This function defines type of differentiable function"""

    a = str(a)
    b = str(b)

    a1 = a.find('x')
    a2 = a.find('y')
    b1 = b.find('x')
    b2 = b.find('y')

    if a1 == -1 and a2 == -1 and b1 == -1 and b2 == -1:
        return(0)
    if (a1 != -1 or b1 != -1) and (a2 != -1 or b2 != -1):
        return(1)
    if (a1 == -1 and b1 == -1) or (a2 == -1 and b2 == -1):
        return(2)

def derivat(z, i):
    """This function considers the derivative"""

    a = sympy.diff(z, i)
    return(a)

def expression_for_classic_function(a, b, Px, Py):
    """This function expresses x through y"""

    sympy.expr = (a - (Px/Py)*b)
    c = sympy.solve(sympy.expr, x)
    e = c.pop()
    e = (e/y)
    return(e)

def budget_for_classic_funcnion(I, e, Px, Py):
    """This function calculates the budget"""

    y = I/(Py + e*Px)
    return(y)

def variable_of_quasilinear_function(a, b):
    """This function defines quasilinear function variable"""

    a = str(a)
    b = str(b)

    a1 = a.find('x')
    a2 = a.find('y')
    b1 = b.find('x')
    b2 = b.find('y')

    if a1 == -1 and b1 == -1:
        return(1)
    if a2 == -1 and b2 == -1:
        return(0)

def expression_for_quasilinear_function(a, b, Px, Py, v):
    """This function expresses a variable in a quasilinear function"""

    sympy.expr = (a/b) - (Px/Py)
    c = sympy.solve(sympy.expr, v)
    e = c.pop()
    return(e)

def budget_for_quasilinear_function(v, c, I, Px, Py):
    """This function calculates the budget of quasilinear function"""

    if v == 0:
        q = I - (c * Px)
        if q <= 0:
            y = 0
            x = I / Px
        else:
            x = c
            y = I - c * Px
    if v == 1:
        q = I - (c * Py)
        if q <= 0:
            x = 0
            y = I / Py
        else:
            y = c
            x = I - c * Py
    return(x, y)

def parsing_of_string(z1):
    """This function divides the mathematical expression into two parts"""

    zf = z1.find('(')
    z1 = z1[(zf + 1):(-1)]
    v_list = list(z1.split(','))
    l_p = v_list[0]
    l_p = eval(l_p)
    r_p = v_list[1]
    r_p = eval(r_p)
    return(l_p, r_p)

import sympy


x = sympy.Symbol('x')
y = sympy.Symbol('y')

Px = float(input('Введите цену фактора x (в ден. ед./шт.):'))
Py = float(input('Введите цену фактора y (в ден. ед./шт.):'))
I = float(input('Введите предполагаемые затраты на факторы производства (в ден. ед.):'))
z1 = (input('Введите производственную функцию от x,y (в ед. продукта):'))

di = diff_or_min(z1)

if di == 0:

    z = eval(z1)
    a = derivat(z, x)
    b = derivat(z, y)

    t = type_diff_f(a, b)

    if t == 0:

        if (a/b) > (Px/Py):
            y = 0
            x = I/Px
            x = round(x, 3)
            y = round(y, 3)

        if (a/b) < (Px/Py):
            x = 0
            y = I/Py
            x = round(x, 3)
            y = round(y, 3)

        if (a/b) == (Px/Py):
            xq = I/Px
            xq = round(xq, 3)
            xq = str(xq)
            yq = I/Py
            yq = round(yq, 3)
            yq = str(yq)
            x = '     ' + xq
            y = 'либо ' + yq
    if t == 1:

        c = expression_for_classic_function(a, b, Px, Py)
        y = budget_for_classic_funcnion(I, c, Px, Py)
        x = y * c
        x = round(x, 3)
        y = round(y, 3)

    if t == 2:

        v = variable_of_quasilinear_function(a, b)
        if v == 0:
            c = expression_for_quasilinear_function(a, b, Px, Py, x)
        if v == 1:
            c = expression_for_quasilinear_function(a, b, Px, Py, y)
        list_answ = budget_for_quasilinear_function(v, c, I, Px, Py)
        x = list_answ[0]
        y = list_answ[1]
        x = round(x, 3)
        y = round(y, 3)

if di == 1:

    list_parts = parsing_of_string(z1)
    l_p = list_parts[0]
    r_p = list_parts[1]
    sympy.expr = (l_p - r_p)
    c = sympy.solve(sympy.expr, x)
    e1 = c.pop()
    e = e1/y
    y = budget_for_classic_funcnion(I, e, Px, Py)
    x = y*e
    x = round(x, 3)
    y = round(y, 3)

print(x, 'ед. фактора x')
print(y, 'ед. фактора y')
