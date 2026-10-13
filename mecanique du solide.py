import sympy as sp
from sympy import *

x = symbols('x')
y= symbols('y')
z=symbols('z') 
d=[symbols('d1'), symbols('d2'),symbols('d3')]

                  

def fonction1(x,y,z):
    a1=symbols('a1') 
    b1= symbols('b1')
    c1=symbols('c1')
    A=matrix_symbols(a1*x+b1*y+c1*z)
    expr = a1*x+b1*y+c1*d(1)
    print(expr)
    
fonction1()