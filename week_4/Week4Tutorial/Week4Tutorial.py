# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 12:00:02 2023

@author: ajult
"""

import io_data_module as iodata
import tkinter

#Open file and read data
data_list = iodata.read_data_file('ellipse1a.txt')
print(data_list)

#Create canvas
top = tkinter.Tk()
C = tkinter.Canvas(top, bg="white", height=700, width=700)

#Display data 
s = 90 #scale factor
r = 2 #radius

#Display data 
for x, y in data_list:
    x = x*s + 150 #some values are negative so +150 is to make them positive
    y = y*s + 150
    C.create_oval(x-2, y-2, x+2, y+2, outline = "red", fill="red")

unknown_sample = (2.236779, 2.896883)
ux = unknown_sample[0]*s + 150
uy = unknown_sample[1]*s + 150
C.create_oval(ux-r, uy-r, ux+r, uy+r)

nearest_sample = iodata.find_nearest_neighbour(unknown_sample, data_list)
nx = nearest_sample[0]*s + 150
ny = nearest_sample[1]*s + 150
C.create_oval(nx-r, ny-r, nx+r, ny+r)

C.create_line(ux, uy, nx, ny, fill="blue")

C.pack()
top.mainloop()


