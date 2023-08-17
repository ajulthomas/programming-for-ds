# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 16:31:18 2021

my_module.py 

@author: milar
"""

def get_grade():
     print('your grade is HD')

def add(a, b):
    return a + b

def get_mark(m):
    s = 'Your mark is ' + str(m)
    return s

__version__ = '0.1'

if __name__ == '__main__':
    print('This is the main program.')    
else:
    print('my_module is imported')
