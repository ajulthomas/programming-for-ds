# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 12:20:22 2023

@author: ajult
"""

# function to calculate the grades
# takes total marks as input
# outputs grade based on the below conditions
# total mark < 50: grade = Fail
# 50 < total mark < 65: grade = P
# 65 < total mark < 75: grade = CR
# 75 < total mark < 85: grade = DI
# total mark > 85: grade = HD
def get_grade(m):
    if m < 50:
        return "Fail"
    elif m>=50 and m<65:
        return "P"
    elif m>=65 and m<75:
        return "CR"
    elif m>=75 and m<85:
        return "DI"
    elif m>=85:
        return "HD"
    
# function to get user input
def get_input():
    return int(input("Enter your total mark: "))

# function to calculate 
# takes grade as input and prints the grade
def get_result(g):
    print(f'Your grade is {g}')

# driver function
def main():
    marks = get_input()
    while marks > 0:
        grade = get_grade(marks)
        get_result(grade)
        marks = get_input()
    print("Exiting the program. Thank you !!!")
   
# starts the program
main()