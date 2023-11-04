"""
                University of Canberra
        Programming for Data Science G (11521) - 2022 (S2)
                    Assignment 3

Question 2 [4 marks] (Tutorials): Implement function load_iris_dataset below that will use the load_iris function and returns 
data, target and target_names as seen in the code below. Use the program below to test your function implementation 
(please do not change the program).

The program with correct function implementation will output the following:
X = [[5.1 3.5 1.4 0.2]
 [4.9 3.  1.4 0.2]
 [4.7 3.2 1.3 0.2]
 [4.6 3.1 1.5 0.2]
 [5.  3.6 1.4 0.2]
 [5.4 3.9 1.7 0.4]
 [4.6 3.4 1.4 0.3]
 ... # some lines deleted to reduce length
 [6.7 3.3 5.7 2.5]
 [6.7 3.  5.2 2.3]
 [6.3 2.5 5.  1.9]
 [6.5 3.  5.2 2. ]
 [6.2 3.4 5.4 2.3]
 [5.9 3.  5.1 1.8]]
y = [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
 2 2]
class labels = ['setosa' 'versicolor' 'virginica']

FAQs:
1. Can I import external libraries? Yes, sklearn and numpy

Marking rubric:
    
Correctly loading iris data- 1 Mark
Correctly outputs for X, y and class_labels 1 Mark each
"""

import numpy

def load_iris_dataset():
       # implement this function here
# end of function

X, y, class_labels = load_iris_dataset()
print('X =', X)
print('y =', y)
print('class labels =', class_labels)
