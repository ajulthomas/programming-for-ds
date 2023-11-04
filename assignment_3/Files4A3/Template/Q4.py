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

iris = datasets.load_iris() # returns np-array (150 rows and 4 columns)

# Each row is a 4D sample
# Column: Sepal Length, Sepal Width, Petal Length and Petal Width.

X = iris.data[:, :2]    # Takes the first two columns
y = iris.target

# Target names: Setosa, Versicolour, and Virginica
labels = iris.target_names

# Plot the data
plt.scatter(X[:, 0], X[:, 1], label='iris', c='r', marker='o', s=30)

plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.title('Iris dataset')
plt.legend()
plt.show()
