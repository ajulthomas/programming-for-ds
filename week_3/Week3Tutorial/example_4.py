# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 12:03:30 2023

@author: ajult
"""

#Example 4
#distance d = square root of (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)
#define function 
def distance(x1, y1, x2, y2):
    d = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return d
#end function

#call function 
x1 = 3
y1 = 0
x2 = 0 
y2 = 4
dist = distance(x1, y1, x2, y2)
print('Distance between (3, 0) and (0, 4) is ' + str(dist))
