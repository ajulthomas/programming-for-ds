# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 18:26:23 2023

@author: ajult
"""

import tkinter as tk
from view.menu import Menu
from view.main import Main
import controller.app_controller as app

class Window(tk.Tk):
    
    def __init__(self, title, size):
        
        super().__init__()
        
        # initial configs
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        
        # variable to hold the dataset input by the user
        self.chosen_dataset = tk.IntVar()
        self.chosen_algorithm = tk.IntVar()
        self.results = {}
        
        # add widgets
        self.menu = Menu(self)
        self.main = Main(self)
        
        # run the ui
        self.mainloop()
        
    def run_algorithms(self, event):
        # chosen dataset value
        cd = self.chosen_dataset.get()
        
        # chosen classification algorithm
        ca = self.chosen_algorithm.get()
        
        # clear previous results
        self.results = {}
        
        print(event)
        print(f"Running algorithms with dataset = {cd}, algorithm = {ca}")
        
        # calling the controller functions to initiate modelling of data
        self.results = app.create_ml_model(cd, ca)
        
        # plot results in main window
        self.main.display_results(self.chosen_algorithm.get(), self.results)