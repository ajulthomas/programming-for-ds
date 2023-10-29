# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 22:08:03 2023

@author: ajult
"""
import tkinter as tk
from tkinter import ttk
import view.configurations as config

import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt

class Main(ttk.Frame):
    def __init__(self, parent):
        
        s = ttk.Style()
        s.theme_use('alt')
        
        s.configure('main.TFrame', background=config.MAIN_BACKGROUND, font=config.APP_FONT, foreground=config.MAIN_FONT_COLOUR, borderwidth=5 )
        s.configure('main.TLabel', background=config.MAIN_BACKGROUND, font=config.MENU_LABEL_FONT, foreground=config.MENU_LABEL_FONT_COLOUR)
        
        super().__init__(parent)
        self.place(relx=0.2, y=0, relwidth=0.8, relheight=1)
        
        # Create a Matplotlib figure and plot the confusion matrix using ConfusionMatrixDisplay
        self.fig = Figure(figsize=(12, 5), dpi=70) 
        self.ax_cm = self.fig.add_subplot(121)
        self.ax_plt = self.fig.add_subplot(122)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        
        # frame to display results
        self.rs_frame = ttk.Frame(self, style="main.TFrame")
        # self.rs_frame.pack(side='top', expand=True, fill="both")
        self.rs_frame.place(relx=0, y=0, relwidth=1, relheight=0.5)
        
        self.rs_frame.columnconfigure((0,1,2), weight = 1, uniform = 'a')
        self.rs_frame.rowconfigure((0,1,2,3,4), weight = 1, uniform = 'a')
        
        # best model
        self.bm = MainLabel(self.rs_frame, text='', position=(0,0,'nw', 1))
        # best params
        self.bp = MainLabel(self.rs_frame, text='', position=(0,1,'nw', 1))
        # best score
        self.bs = MainLabel(self.rs_frame, text='', position=(0,2,'nw', 1))
        # model accuracy
        self.model_accuracy = MainLabel(self.rs_frame, text='', position=(1,0,'nw', 1))
        
        # classification report
        # Create a Text widget to display the classification report
        self.clfr = tk.Text(self.rs_frame, 
                            wrap=tk.WORD, 
                            width=58, 
                            height=10, 
                            bg=config.MAIN_BACKGROUND, 
                            fg=config.MENU_LABEL_FONT_COLOUR, 
                            highlightthickness=0,
                            bd=0.5
                            )
        self.clfr.grid(row=1 , column=1, sticky='ne', columnspan=2, rowspan=2)
        
        # model predictions
        # self.model_predictions = MainLabel(self.rs_frame, text='', position=(4,0,'nw', 3), rowspan=2)
        self.model_predictions = tk.Text(self.rs_frame, 
                            wrap=tk.WORD, 
                            width=150, 
                            height=8, 
                            bg=config.MAIN_BACKGROUND, 
                            fg=config.MENU_LABEL_FONT_COLOUR, 
                            highlightthickness=0,
                            bd=0.5
                            )
        self.model_predictions.grid(row=3 , column=0, sticky='sw', columnspan=3, rowspan=2, padx=4, pady=8)
        
    # updates results in ui
    def update_results(self, results):
        self.bm.configure(text=f'Best Model:\n{results["best_model"]}')
        # best params
        self.bp.configure(text=f'Best parameters: \n{results["best_params"]}')
        # best score
        self.bs.configure(text=f'Best Score: \n{results["best_score"]}')
        # model accuracy
        self.model_accuracy.configure(text=f'Model accuracy: \n{results["accuracy"]:.2f} %')
        # classification report
        MainLabel(self.rs_frame, text='Classification Report :', position=(1,1,'nw', 1))
        # Display the classification report in the GUI
        self.clfr.delete(1.0, tk.END)  # Clear any previous content
        self.clfr.insert(tk.END, results['cfr'])
        
        # model predictions
        MainLabel(self.rs_frame, text='Test Data and Model predictions :', position=(2,0,'sw', 1))
        # self.model_predictions.configure(text=f'{results["test_pred"].T.to_string(header=False)}')
        # Display the model predictions in the GUI
        self.model_predictions.delete(1.0, tk.END)  # Clear any previous content
        self.model_predictions.insert(tk.END, results['test_pred'].T.to_string(header=False))

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
        self.plot_cm(results['cmd'])    
        
        # plots graph
        self.plot_params_graph(chosen_algorithm, results['results'])
            
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side='bottom', expand=False, fill='x')
        self.toolbar.pack(side='bottom')
        
        # print the results to frame
        self.update_results(results)
    ### end of function
    ### end of class definition
        

    # plots confusiion matrix
    def plot_cm(self, cm):
         
        # plot the confusion matrix
        cm.plot(cmap='Blues', ax=self.ax_cm)
        
        self.ax_cm.set_title('Confusion Matrix')
    ### end of function        
        
        
    def plot_params_graph(self, chosen_algorithm, results):     
        if(chosen_algorithm == 0):
            # selecting the required params for the y axis
            y = results[['mean_test_score']]
            # print(y)
            # selecting the required params for the x axis
            x = results[['param_n_neighbors']]
            # print(x)
            # plotting the results 
            self.ax_plt.plot(x, y)
            # set title
            self.ax_plt.set_title('Cross Validation plot for KNN')
            # set label for the y axis
            self.ax_plt.set_ylabel('Cross-Validated Accuracy')
            # set label for the x axis
            self.ax_plt.set_xlabel('Value of K for KNN')
        else:
            # selecting required params for the y axis
            x= results['param_gamma'].unique()
            # print(x)
            # selecting the required params for the y axis
            y_1 = results[results['param_C'] == 0.1]['mean_test_score']
            y_2 = results[results['param_C'] == 1]['mean_test_score']
            y_3 = results[results['param_C'] == 10]['mean_test_score']
            y_4 = results[results['param_C'] == 100]['mean_test_score']
            # plotting the results 
            self.ax_plt.semilogx(x, y_1, marker='o', linestyle='--', color='b', label="c = 0.1")
            self.ax_plt.semilogx(x, y_2, marker='o', linestyle='--', color='g', label="c = 1")
            self.ax_plt.semilogx(x, y_3, marker='o', linestyle='--', color='r', label="c = 10")
            self.ax_plt.semilogx(x, y_4, marker='o', linestyle='--', color='orange', label="c = 100")
            # set title
            self.ax_plt.set_title('Cross Validation Plot for SVM')
            # set label for the y axis
            self.ax_plt.set_ylabel('CV score')
            # set label for the x axis
            self.ax_plt.set_xlabel('Parameter gamma (log scale)')
            # show legends
            self.ax_plt.legend()
     ### end of function
        
        
class MainLabel(ttk.Label):
    def __init__(self, parent, text, position, rowspan=1):
        # s = ttk.Style()
        # s.configure('menuLabel.TLabel', foreground = "#001011")
        super().__init__(parent, text=text, style="main.TLabel")
        # self.pack(side= position, expand=expand, fill=fill, pady=5 )
        self.grid(row=position[0] , column=position[1], sticky=position[2], columnspan=position[3], rowspan=rowspan, padx=10, pady=10)