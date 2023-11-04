"""
                University of Canberra
        Programming for Data Science G (11521) - 2022 (S2)
                    Assignment 3

Question 5 [8 marks] (Pandas): Implement a program that uses Pandas package to input data from mycsv.csv and output
data to myexcel.xls file (2 sheets). Download these files from Assignment 3 module from the ‘Modules’ page in Canvas
site.
The data to be input from mycsv.csv are from the following selected columns and rows:
• Columns: only 4 columns with the following headers SIS User ID, Submit Assignment 1 (57584),
Submit Assignment 2 (57585), and Submit Assignment 3 (57473)
• Rows: only rows that have ID value in column SIS User ID. Those ID values start with either letter u (e.g., u123456)
or letter s (e.g., s123484). Other ID values are ignored.
You will write code to change column headers as follows:
• Change SIS User ID to StudentID
• Change Submit Assignment 1 (57584) to Ass1
• Change Submit Assignment 2 (57585) to Ass2, and
• Change Submit Assignment 3 (57473) to FE.
You will also write code to separate data in to 2 groups (group 1: ID starting with u and group 2: ID starting with s).
Hint: Remove rows that do not contain id’s starting with ‘s’ or ‘u’ and perform row selection via string match.
Arrange the ‘s’ group data in the descending order of A2, and ‘u’ group data in the ascending order of FE.
The data to be output to sheets named `UID’ and `SID’ respectively in myexcel.xls are the sorted ‘s’ and ‘u’ group data
• Sheet UID: columns: StudentID, Ass1, Ass2, and FE, and rows: only rows that have ID value starting with letter u.
• Sheet SID: columns: StudentID, Ass1, Ass2, and FE, and rows: only rows that have ID value starting with letter s.

Expected output: Please refer the Instructions document (PDF)

FAQs:
1. I'm getting an error saying 'xlwt module not found'.
you will need to run ‘pip install xlwt’ in your Conda virtual environment and add ‘import xlwt’ at the beginning of
your python code. We hope that by now you are familiar with installing python packages in your machine.

Marking rubric:

Reading Dataframe (df) from csv file: 1 Mark    
Correctly modifying df columns:       2 Marks
Segregating 's', 'u' groups:          2 Marks
Sorting 's', 'u' groups:              2 Marks 
Writing S, U Data onto Excel:         1 Mark       
"""

# Your code here

import pandas as pd
# import xlwt

# read csv file
data = pd.read_csv('Files4A3/mycsv.csv')

# subsetting the data frame to have the required columns only
df = data.loc[:, ['SIS User ID', 'Submit Assignment 1 (57584)', 'Submit Assignment 2 (57585)', 'Submit Assignment 3 (57473)']]

# print the top 5 rows
# df.head()

# change the column names
# creates a dictionary to map old column names to new column names
new_col_names = {
    'SIS User ID': 'StudentID', 
    'Submit Assignment 1 (57584)': 'Ass1', 
    'Submit Assignment 2 (57585)': 'Ass2', 
    'Submit Assignment 3 (57473)': 'FE', 
    }

# uses the rename() method to rename the columns
df = df.rename(columns=new_col_names)

# Remove rows with NA values in the "Student ID" column
df = df.dropna(subset=['StudentID'])

# Remove rows where "Student ID" doesn't start with 'u' or 's'
df = df[df['StudentID'].str.startswith(('u', 's'))]


# Update data types of columns
df['StudentID'] = df['StudentID'].astype('string')
df['Ass1'] = df['Ass1'].astype('float')
df['Ass2'] = df['Ass2'].astype('float')
df['FE'] = df['FE'].astype('float')


# splits data into two dataframes based on student ID
df_s = df[df['StudentID'].str.startswith('s')]
df_u = df[df['StudentID'].str.startswith('u')]


# sorts the ‘s’ group data in the descending order of A2(Ass2)
df_s = df_s.sort_values(by='Ass2', ascending=False)


# sorts the ‘u’ group data in the ascending order of FE
df_u = df_u.sort_values(by='FE', ascending=True)


# writes sorted data to two excel sheets
with pd.ExcelWriter('output/myexcel.xlsx') as excl:
    df_u.to_excel(excl, sheet_name='UID', index=False)  # 'u' group data in 'UID' sheet
    df_s.to_excel(excl, sheet_name='SID', index=False)  # 's' group data in 'SID' sheet
