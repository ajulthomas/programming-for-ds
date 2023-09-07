# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 12:56:10 2023

@author: ajult
"""

from tkinter import *
top = Tk()

#add code in next steps below this line

# draw a line between two points (x1, y1) and (x2, y2)
C = Canvas(top, bg="white", height=700, width=700)
x1 = 100
y1 = 100
x2 = 200
y2 = 300
C.create_line(x1, y1, x2, y2, fill = "blue")

# draw a circle at point (x1, y1) with radius 2
C.create_oval(x1-2, y1-2, x1+2, y1+2, outline = "red", fill="red")
C.create_oval(x2-2, y2-2, x2+2, y2+2, outline = "red", fill="red")


C.pack()
top.mainloop()
