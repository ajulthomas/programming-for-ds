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
