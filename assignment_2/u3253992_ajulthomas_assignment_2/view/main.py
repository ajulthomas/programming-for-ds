# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 22:08:03 2023

@author: ajult
"""

from tkinter import ttk

class Main(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.place(relx= 0.3, y = 0, relwidth = 0.7, relheight = 1)