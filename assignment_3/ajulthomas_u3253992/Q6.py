"""
               University of Canberra
        Programming for Data Science G (11521) - 2022 (S2)
                    Assignment 3

Question 6 [4 marks] (Matplotlib): Implement a program that uses Matplotlib and Pandas packages to read data from 2
sheets in myexcel.xls and plots histograms as per the outputs below for the distributions of Ass1, Ass2 and FE,
in sheets UID and SID. Expected outputs with number of bins = 20 and face colours of blue, green, and red respectively
for Ass1, Ass2 and FE.

FAQs: Use Matplotlib and Pandas packages only

Marking rubric:
1. Reading dataframe (df) from Excel file: 1 Mark
2. Processing df columns apprpriately:     1 Mark
3. Plotting S,U Histograms with bins=20:   2 Marks (1 each for S and U)
   and visualized face colors 

"""


import matplotlib.pyplot as plt
import pandas as pd

# read the excel sheet SID
# reference: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
df_s = pd.read_excel('output/myexcel.xlsx', sheet_name='SID')

# read the excel sheet UID
df_u = pd.read_excel('output/myexcel.xlsx', sheet_name='UID')

# print(df_s)
# print(df_u)

# craete subplots
fig, axes = plt.subplots(2, 3, figsize=(12, 6))

columns_to_plot = df_s.columns[1:]

colours = ['b', 'g', 'r']

for i in range(3):
    
    # selelcts the subplot
    
    # plots on row1 for S group
    ax1 = axes[0,i]
    
    # plots on row2 for U group
    ax2 = axes[1,i]
    
    # selects the column to plot 
    col = columns_to_plot[i]
    
    # x-axis label
    x_label = 'Marks'
    
    # y axis label
    y_label = 'Probability'
    
    # title for S group
    title_s = f'S group: {col}'
    
    # title for U group
    title_u = f'U group: {col}'
    
    # plots the variable
    ax1.hist(df_s[[col]], 20, density=1, facecolor=colours[i], alpha=0.7)
    ax1.set_title(title_s)   # sets title of the plot
    ax1.set_xlabel(x_label)  # sets x-axis label
    ax1.set_ylabel(y_label)  # sets y-axis label
   
    
    # plots the variable
    ax2.hist(df_u[[col]], 20, density=1, facecolor=colours[i], alpha=0.7)
    ax2.set_title(title_u)  # sets title of the plot
    ax2.set_xlabel(x_label) # sets x-axis label
    ax2.set_ylabel(y_label) # sets y-axis label


# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()
