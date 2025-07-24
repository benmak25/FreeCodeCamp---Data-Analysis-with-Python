import numpy as np

def calculate(list):
    calculations = {}

    if (len(list) != 9): #Checks if input is valid, if not, return an Error
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(list).reshape(3,3)

    #Calculating all necessary values, while converting from numpy array to list values
    mean_list = [matrix.mean(axis = 0).tolist() , matrix.mean(axis = 1).tolist() , matrix.mean().tolist() ]
    std_list = [matrix.std(axis = 0).tolist() , matrix.std(axis = 1).tolist() , matrix.std().tolist() ]
    var_list =  [matrix.var(axis = 0).tolist() , matrix.var(axis = 1).tolist() , matrix.var().tolist() ]
    min_list = [matrix.min(axis = 0).tolist() , matrix.min(axis = 1).tolist() , matrix.min().tolist() ]
    max_list = [matrix.max(axis = 0).tolist() , matrix.max(axis = 1).tolist() , matrix.max().tolist() ]
    sum_list = [matrix.sum(axis = 0).tolist() , matrix.sum(axis = 1).tolist() , matrix.sum().tolist() ]

    #Inputting values into the dictionary
    calculations['mean'] = mean_list
    calculations['variance'] = var_list
    calculations['standard deviation'] = std_list
    calculations['min'] = min_list
    calculations['max'] = max_list
    calculations['sum'] = sum_list



    return calculations
