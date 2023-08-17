# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 10:30:18 2021

*** Programming for Data Science ****

Examples Week 3 - Modules

@author: Dr. Raul Fernandez-Rojas
"""

# Definde working directory
import os
os.chdir('D:\\Files\\Raul\\Python\\PDS\\')  #selec *your own* working directory


#*************** Functions *****************
# Example 1: Add import statement to use function in modules
# Import module 
import my_module

sum = my_module.add(5, 7)
print(sum)

my_module.get_grade()

mark = my_module.get_mark(88)
print(mark)


# Example 2: Add from .. import * statement to use function in modules
# Import module
from my_module import *

sum = add(5, 7)
print(sum)

get_grade()

mark = get_mark(88)
print(mark)


# Example 3: Add specific function from module
# Import module support
from my_module import add

sum = add(5, 7)
print(sum)

# Example 4: Add specific function from module
# run the my_module.py file as standalone 
runfile('D:/Files/Raul/Python/PDS/my_module.py')  #change to your path

# Now try again to import the module
#from my_module import add

# Running it as standalone by the user 
if __name__ == '__main__':
    print('This is the main program.')
else:
    print('my_module is imported')

sum = add(5, 7)
print(sum)
get_grade()
mark = get_mark(88)
print(mark)



#*************** Inputs and Outputs *****************
# Example 1: Data from/to file

# data to be saved
data = '''1.23, 2.15, 3.11
1.21, 1.13, 1.46
2.13, 3.11, 2.12
'''

# Open for writing
f = open('data.txt', 'w')

# Write text to file
f.write(data)

# Close the file
f.close()

# now, let's read the saved data
f = open('data.txt', 'r')
while True:
    line = f.readline()
    print(line + ' ')
    # Zero length indicates EOF
    if len(line) == 0:
        break
# Note the line already has a newline character \n at the end of each line since it is reading from a file.

# Close the file
f.close()


# Example: store as numeric value
number = 1337

# Open for writing
f = open('my_number.txt', 'w')

# Write data to file
f.write('%d' % number)
# Close the file
f.close()


# now, let's read the saved data
f = open('my_number.txt', 'r')
while True:
    line = f.readline()
    print(line)
    # Zero length indicates EOF
    if len(line) == 0:
        break

# Close the file
f.close()


# Example 2: Unicode data from/to file
# UTF (Unicode Transformation Format)

# encoding=utf-8
import io

# write data to file
f = io.open("utf8.txt", "wt", encoding="utf-8")

f.write(u"Programmierung für Data Science (German)\nProgrammation pour la science des données (French)")
f.close()

#read data from file
f = io.open("utf8.txt", encoding="utf-8")
print(f.read())
f.close()


#*************** Pickle File *****************
# Example 1: Pickle file

import pickle

# Name the file for storing data
studyfile = 'assessments.data'
# Name the list of assessments
assessments = ['tutorials', 'assignments', 'online test', 'exam']

# Open the file for writing
f = open(studyfile, 'wb')
# Write the list to the file
pickle.dump(assessments, f)
f.close()
# Destroy the list
del assessments

# Read back from the file
f = open(studyfile, 'rb')
# Load the object from the file
assessments = pickle.load(f)
print(assessments)
f.close()



#*************** Exception Handling *****************
# Example 1: Zero division error
try:
    a = 2
    b = 0
    c = a / b
except ZeroDivisionError:  # this is a build-in exception
    print('You cannot divide a number by 0')
else:
    print(c)


# Example 2: get message from python
try:
    a = 'xy'
    b = 'y'
    c = a / b
except Exception as error:
    print(error.args)
else:
    print(c)


# Example 3: try.. except.. finally
try:
    print('ourVariable')
except:
    print('ourVariable is not defined')
finally:
    print('Code has been run.')


# Example 4:
try:
  print(x)
except NameError:   # this is a build-in exception
  print("Variable x is not defined")
except:
  print("Something else went wrong")
  
    
# Example 5: 
# define function to print number
def do_stuff_with_number(n):
    print(n)

# create a list with inly 5 elements
the_list = (1, 2, 3, 4, 5)

for i in range(10): # we are trying to access more than 5 elements, thus, an error
    try: # no problem
        do_stuff_with_number(the_list[i])  
    except IndexError: # Raised when accessing a non-existing index of a list. This is a build-in exception
        do_stuff_with_number(0)


# Example 6: Habdling multiple errors
def example6():
    while True: # so it repeates until numbers are correct
       try:
            x = int( input( "enter first number: " ) )
            y = int( input( "enter second number: " ) )
            print( x, '/', y, '=', x/y )        
            break
       except ZeroDivisionError:  # this is a build-in exception
            print( "Can't divide by 0!" )
       except ValueError:   # this is a build-in exception
            print( "That doesn't look like a number!" )
       except:
            print( "something unexpected happend!" )

# run example
example6()
