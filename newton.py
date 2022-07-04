import math
import sympy as sp

def newton(f,Df,x0,epsilon,max_iter):
    
    
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Derivada de f(x) = 0. Sem solução possível')
            return None
        xn = xn - fxn/Dfxn
    print('Sem solução n, tal que f(n) < ', epsilon, ' após ', n + 1, ' Iterações')
    return None

if __name__ == '__main__': 
    x = sp.symbols('x')

    a = lambda x: 2*(x**3) - 5*(x**2) - x + 3
    b = lambda x: 5*(x**3) - 2*(x**2) - 8*x + 10 

    da = lambda x: 6*(x**2) - 10*x - 1
    db = lambda x: 15*(x**2) - 4*x - 8

    ans_a = newton(a,da, 1, 10**-5, 50)
    ans_b = newton(b, db,-1, 10**-7, 50)

    print("a) ",ans_a , " Erro: ", (a(ans_a)))
    print("b) ",ans_b , " Erro: ", (b(ans_b)))