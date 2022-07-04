import numpy as np
import pandas as pd
import argparse 

def argCli(): 
    argParser = argparse.ArgumentParser()

    argParser.add_argument('--list', '-l', nargs='+', required=True, help='List of polynom expoens, where element C with index i represents C * x^i')
    argParser.add_argument('--value', '-v', required=True, help='Value for parameter of polynomial')

    args = vars(argParser.parse_args())
        
    if 'list' in args: 
        listArg = args['list']
        listArg = np.array(listArg)
#        listArg = listArg.astype(dtype=float)

        args['polynomial'] = pd.to_numeric(listArg)

        del args['list']
    
    return args