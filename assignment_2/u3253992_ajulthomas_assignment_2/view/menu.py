# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 21:44:37 2023

@author: ajult
"""

from tkinter import ttk

import view.configurations as config

class Menu(ttk.Frame):
        
    def __init__(self, parent):
        
        s = ttk.Style()
        s.theme_use('alt')
        s.configure('menu.TFrame', background=config.MENU_BACKGROUND, font=config.APP_FONT, foreground=config.MENU_FONT_COLOUR, borderwidth=5 )
        s.configure('submenu.TFrame', background=config.TEST_BACKGROUND)
        s.configure('menu.TRadiobutton', background=config.MENU_BACKGROUND, font=config.APP_FONT, foreground=config.MENU_FONT_COLOUR, borderwidth=0, focusthickness=3, focuscolor='none')
        s.configure('menu.TLabel', background=config.MENU_BACKGROUND, font=config.APP_FONT, foreground=config.MENU_FONT_COLOUR)
        s.configure('menu.TButton', background=config.BUTTON_BACKGROUND, foreground=config.BUTTON_FORGROUND, font=config.APP_HEADINGS_FONT, borderwidth=0, focusthickness=3, focuscolor='none')
        s.map('menu.TButton', background=[('active',config.BUTTON_BACKGROUND)])
        
        super().__init__(parent, style="menu.TFrame")
        self.place(x = 0, y = 0, relwidth = 0.2, relheight = 1)
        
        self.columnconfigure((0,1,2), weight = 1, uniform = 'a')
        self.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight = 1, uniform = 'a')
        
        
        self.create_cd_widgets(parent)
        self.create_ca_widgets(parent)
        
        run_btn = ttk.Button(self, text="Run", style="menu.TButton")
        run_btn.grid(row=6, column=1, sticky='nw', columnspan=1, ipadx=10, ipady=10)
        run_btn.bind("<Button-1>", parent.run_algorithms)
        
    # create widgets to choose the dataset    
    def create_cd_widgets(self, window_ref):
        cd_label = MenuLabel(parent=self, text="Choose Dataset", position=(1,0, 'w', 3))
        
        # create a frame to contain the radio buttons
        cd_frame = ttk.Frame(self, style="menu.TFrame")
        cd_frame.grid(row=2, column=0, sticky='nw', columnspan=3, rowspan=2)
        
        # configs the grid
        cd_frame.rowconfigure((0,1,2), weight = 1, uniform = 'a')
        cd_frame.columnconfigure(1, weight=1, uniform='a')
        
        # 
        iris_rb = ttk.Radiobutton(master=cd_frame, text="Iris Dataset", value=0, variable=window_ref.chosen_dataset, style="menu.TRadiobutton")
        iris_rb.grid(row=0,column=0,sticky='nw')
        
        #
        breast_cancer_rb = ttk.Radiobutton(master=cd_frame, text="Breast Cancer Dataset", value=1, variable=window_ref.chosen_dataset, style="menu.TRadiobutton")
        breast_cancer_rb.grid(row=1,column=0,sticky='nw')
        
        #
        wine_rb = ttk.Radiobutton(master=cd_frame, text="Wine Dataset", value=2, variable=window_ref.chosen_dataset, style="menu.TRadiobutton")
        wine_rb.grid(row=2,column=0,sticky='nw')
        
    # create widgets to choose the algorithms
    def create_ca_widgets(self, window_ref):
        ca_label = MenuLabel(parent=self, text="Choose the classification Algorithm:", position=(3,0,'w',3))
        
        # create a frame to contain the radio buttons
        ca_frame = ttk.Frame(self, style="menu.TFrame")
        ca_frame.grid(row=4, column=0, sticky='nw', columnspan=3, rowspan=2)
        
        # 
        knn_rb = ttk.Radiobutton(master=ca_frame, text="K-Nearest Neighbours Classification", value=0, variable=window_ref.chosen_algorithm, style="menu.TRadiobutton")
        knn_rb.grid(row=0,column=0,sticky='nw')
        
        #
        svc_rb = ttk.Radiobutton(master=ca_frame, text="Support Vector Classification", value=1, variable=window_ref.chosen_algorithm, style="menu.TRadiobutton")
        svc_rb.grid(row=1,column=0,sticky='nw')

class MenuLabel(ttk.Label):
    def __init__(self, parent, text, position):
        # s = ttk.Style()
        # s.configure('menuLabel.TLabel', foreground = "#001011")
        super().__init__(parent, text=text, style="menu.TLabel")
        self.grid(row=position[0] , column=position[1], sticky=position[2], columnspan=position[3])
        