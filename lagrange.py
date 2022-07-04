import numpy as np
import pandas as pd
import argparse

# Process Command line arguments
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

# Calculate solution's bounds for positive roots(if existis). 
def __calculatePositiveBound__(polynomial=np.array([])): 
    raise TypeError('Function not implemented')

# Calculate solution's bounds for negative roots(if existis). 
def __calculateNegativeBounds__(polynomial=np.array([])): 
    raise TypeError('Function not implemented')

# Calculate Upper bounds of a polynomial function f(x) roots (if exists)
def __calculateUpperBound__(polynomial=np.array([])):
    raise TypeError('Function not implemented')

# Calculate Lower bounds of a polynomial function f(x) roots (if exists)
def __calculateLowerBound__(polynomial=np.array([])):
    raise TypeError('Function not implemented')

# Calculate Positive (Upper and Lower) and Negative (Upper and lower) bounds of a polynomial function's roots(If existis). 
def calculateBounds(polynomial=np.array([])): 
    if polynomial[0] < 0:
        arr = getInverseFunction(polynomial)
        print(arr)
    else:
        print(polynomial)

#get f(x) * -1
def getInverseFunction(polynomial): 
    f = lambda x: -x

    ans = f(polynomial)
    return ans

# Get f(-x)
def getNegativePolynomial(polynomial=np.poly1d([])):
    raise NotImplementedError

# Calculate Lagrange 
def processLagrange(list=np.array([])): 
    if list.size == 0:
        raise TypeError('Polynomial values are Required')

    polynomial = np.poly1d(list)


    #TO DO: CALCULAR OS LIMITES SUPERIORES E INFERIORES DA SOLUÇÃO

if __name__ == '__main__':
    processLagrange(**argCli())