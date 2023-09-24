# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 12:08:07 2023

@author: ajult
"""

#Function to read multi-dimensional data from file and 
#return data as a list of tuples
def read_multi_dim_data_file(filename):
    
    dataset = {} #dataset is a python list 
    f = None
    try:
        f = open(filename, 'r')
        while True:
            line = f.readline()
            if len(line) == 0: #end of file
                break
            line = line.replace('\n', '') #remove end of line \n character
            string_list = line.split(',') # coordinates in string format
            if len(string_list) < 2: #empty line
                continue #skip it
                
            # extracting the key name
            iris_type = string_list[-1]
            #print("irirs type : ", iris_type)
            
            if iris_type not in dataset:
                dataset[iris_type] = []
            
            string_sublist = string_list[:-1]
            
            sublist = [float(x) for x in string_sublist]
            
            dataset[iris_type].append(tuple(sublist))
            
    except Exception as ex:
        print(ex.args)
    finally:
        if f:
            f.close()
    return dataset
#end of function
