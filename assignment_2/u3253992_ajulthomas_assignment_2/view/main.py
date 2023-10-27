# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 22:08:03 2023

@author: ajult
"""

from tkinter import ttk
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt

class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.2, y=0, relwidth=0.8, relheight=1)
        
        # Create a Matplotlib figure and plot the confusion matrix using ConfusionMatrixDisplay
        self.fig = Figure(figsize=(12, 6), dpi=75) 
        self.ax_cm = self.fig.add_subplot(121)
        self.ax_plt = self.fig.add_subplot(122)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)

    # prints results on screen, plots graphs
    def display_results(self,chosen_algorithm, results):
        # remove previous image
        if(self.fig):
            self.fig.clf()
            self.ax_cm.clear()
            self.ax_cm = self.fig.add_subplot(121)
            self.ax_plt.clear()
            self.ax_plt = self.fig.add_subplot(122)
        
        if (self.canvas):
            self.canvas.get_tk_widget().pack_forget()  
            self.canvas.get_tk_widget().delete("all")
            
        # plots confusion matrix
        self.plot_cm(results['confusion_matrix'])    
        
        # plots graph
        self.plot_params_graph(chosen_algorithm, results['results'])
            
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side='top', expand=False, fill='x')
    ### end of function
        

    # plots confusiion matrix
    def plot_cm(self, cm):
         
        # plot the confusion matrix
        cm.plot(cmap='Blues', ax=self.ax_cm)
        
        self.ax_cm.set_title('Confusion Matrix')
    ### end of function        
        
        
    def plot_params_graph(self, chosen_algorithm, results):     
        y = results[['mean_test_score']]
        print(y)
        
        if(chosen_algorithm == 0):
            x = results[['param_n_neighbors']]
            print(x)
            self.ax_plt.plot(x, y)
            self.ax_plt.set_title('Cross Validation plot for KNN')
            self.ax_plt.set_ylabel('Cross-Validated Accuracy')
            self.ax_plt.set_xlabel('Value of K for KNN')
        else:
            x= results[['param_C']]
     ### end of function   
        
        
