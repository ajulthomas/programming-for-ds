# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 18:26:23 2023

@author: ajult
"""

import tkinter as tk
from menu import Menu
from main import Main


class Window(tk.Tk):
    
    def __init__(self, title, size):
        
        super().__init__()
        
        # initial configs
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        
        # variable to hold the dataset input by the user
        self.chosen_dataset = tk.IntVar()
        self.chosen_algorithm = tk.IntVar()
        
        # add widgets
        self.menu = Menu(self)
        self.main = Main(self)
        
        # run the ui
        self.mainloop()
        
    def run_algorithms(self):
        pass
