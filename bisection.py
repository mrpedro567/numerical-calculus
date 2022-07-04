import numpy as np
import math
import pandas as pd
import argparse


def argCli():
    argParser = argparse.ArgumentParser()

    argParser.add_argument('--list', '-l', nargs='+', required=True, help='List of polynom expoens, where element C with index i represents C * x^i')

    args = vars(argParser.parse_args())
        
    if 'list' in args: 
        listArg = args['list']
        listArg = np.array(listArg)
#        listArg = listArg.astype(dtype=float)

        args['polynomial'] = pd.to_numeric(listArg)

        del args['list']
    
    return args

'''
    Parametros: 
        f: function f(x)
        a, b: intervalo [a, b] para procurar a raiz
		N: Número máximo de Iterações
        e: erro
'''
def bisection(f,a,b,N,e):
    # f(a) * f(b) < 0; 
    if f(a)*f(b) >= 0:
        print("f(a)*f(b) >= 0, não é possivel procurar raiz no intervalo [a, b].")
        return None

    a_n = a
    b_n = b
    
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            #print(m_n, " f(x)=0")
            return m_n
        elif f(m_n) < e:
            #print(m_n, " f(x) < ", e)
            return m_n
        else: 
            return None
    
    #print(m_n, " Valor mais próximo após ", N, " iterações")
    return (a_n + b_n)/2


if __name__ == '__main__':
    f = lambda x: 2*(x**3) - 5*(x**2) - x + 3
    f_2 = lambda x: 5*(x**3) - 2*(x**2) - 8*x + 10    
    
    a = bisection(f, 0, 1, 50,10**-5)
    b = bisection(f_2, -2, -1, 50, 10**-7)

    print("a) ",a , " Erro: ", (f(a)))
    print("b) ",b , " Erro: ", (f_2(b)))
