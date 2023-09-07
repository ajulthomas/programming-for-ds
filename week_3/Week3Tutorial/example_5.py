# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 12:04:53 2023

@author: ajult
"""

#Example 5
#distance d = square root of (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)
#Two points are two tuples p1 = (x1, y1) and p2 = (x2, y2)
#define function 
def distance(p1, p2):
    d = 0
    for i in range(len(p1)):
        d += (p2[i] - p1[i])**2 
    d = d**0.5
    return d
#end function
#call function 
#Two points are two tuples (x, y)
p1 = (3, 0)
p2 = (0, 4)
dist = distance(p1, p2)
print('Distance between p1 and p2 is ' + str(dist))
