# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:59:15 2023

@author: ajult
"""

#Function to read 2D data from file and save data to a list of tuples
def read_data_file(filename):
    dataset = [] #dataset is a python list 
    f = None
    try:
        f = open(filename, 'r')
        while True:
            line = f.readline()
            if len(line) == 0: #end of file
                break
            line = line.replace('\n', '') #remove end of line \n character
            xystring = line.split(' ') #x y coordinates in string format 
            #use split function to separate x & y strings then 
            #use float function to convert x & y strings to x & y numbers and 
            #add them as a tuple (x, y) to dataset that is a list
            dataset.append((float(xystring[0]), float(xystring[1])))
    except Exception as ex:
        print(ex.args)
    finally:
        if f:
            f.close()
    return dataset
#end of function


#define function
def find_nearest_neighbour(unknown_sample, data_list):
    shortest_distance = get_distance(data_list[0][0], data_list[0][1], unknown_sample[0], unknown_sample[1])
    nearest_point = None
    #write your code here
    for x,y in data_list:
        distance = get_distance(x, y, unknown_sample[0], unknown_sample[1])
        if(shortest_distance > distance):
            shortest_distance = distance
            nearest_point = (x,y)
    print(f'Nearest {nearest_point}')
    return { nearest_point: nearest_point, distance: shortest_distance }
#end function


def get_distance(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
