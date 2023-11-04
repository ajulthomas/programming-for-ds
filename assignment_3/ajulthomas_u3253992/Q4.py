"""
                University of Canberra
        Programming for Data Science G (11521) - 2022 (S2)
                    Assignment 3

Question 4 [8 marks] (NumPy): Below is the program you used in Example 14 in Week 10 Tutorial. In that example,
the first two columns of data in Iris dataset were selected for plotting:

X = iris.data[:, :2]

Your tasks for this question are as follows.
• Remove X = iris.data[:, :2], plt.xlabel('Sepal length') and plt.ylabel('Sepal width') from the program.
• Add import numpy as np
• Add your code to ask the user to input 2 numbers between 0 and 3 inclusive.
• Use the two input numbers as column indices and built-in functions in NumPy package to
implement the program to select 2 columns of data from the four columns in the Iris
dataset and update xlabel and ylabel accordingly.
• Please do not use Pandas or other additional packages. Only Numpy package is imported.

Expected output: Please refer the instructions file (PDF).

FAQs:
1. Can I import external libraries, for example pandas or numpy?
You are allowed to use ONLY numpy, and not any other packages.

Marking rubric:

Input attribute columns from from user - 2 Marks
Getting the correct feature matrix     - 2 Marks
Generating expected visualization      - 4 Marks
"""

import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np

iris = datasets.load_iris() # returns np-array (150 rows and 4 columns)

# Each row is a 4D sample
# Column: Sepal Length, Sepal Width, Petal Length and Petal Width.


# gets user input to select the features to be plotted
def get_user_input(i):
    # infinite loop 
    while True:
        # getting user input
        index = int(input(f'Select feature {i} (enter a number between 0 and 3) : '))
        
        # if index out of bound, show error and ask user to enter again
        if((index < 0) or (index > 3)):
            print(f'Error: Selected feature index {index} is outside the expected range. Kindly provide the values again')
        
        # if endex witin bounds break out of the loop 
        else:
            break
        
    # returns user input
    return index

# gets feature to be plotted on x -axis
f1=get_user_input(1)

# gets feature to be plotted on y axis
f2=get_user_input(2)

# X = iris.data[:, :2]    # Takes the first two columns
X = iris.data[:, [f1, f2]]
y = iris.target

# Target names: Setosa, Versicolour, and Virginica
labels = iris.target_names

# Plot the data
plt.scatter(X[:, 0], X[:, 1], label='iris', c='r', marker='o', s=30)

# dynamically selelct the feature names according to the selected column
plt.xlabel(iris.feature_names[f1].capitalize())
plt.ylabel(iris.feature_names[f2].capitalize())

plt.title('Iris dataset')
plt.legend()
plt.show()


    
    
    