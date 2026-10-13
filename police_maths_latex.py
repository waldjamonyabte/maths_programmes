from sympy import symbols, sin, Integral, expand, latex
from IPython.display import display

x = symbols('x')
expr = Integral(sin(x) / x, x)

display(expr)


def fonction1():
    x = symbols('x')
    expr = (x + 1) ** 5
    print(latex(expr))


def fonction2():
    x = symbols('x')
    expr = expand((x + 2) ** 4)
    print(latex(expr))


if __name__ == '__main__':
    fonction1()
    fonction2()
