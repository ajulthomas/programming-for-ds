# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 12:50:52 2023

@author: ajult
"""

#Question 4:
#define function 
#write your function find_max here
def find_max(*argv):
    max = argv[0]
    for arg in argv:
        if max < arg:
            max = arg
    return max
#end of function 

max = find_max(2, 4, 8, 3, 1, 33, 25, 65)
print('Maximum value is ' + str(max)) 

max = find_max(36, 52, 65)
print('Maximum value is ' + str(max))
