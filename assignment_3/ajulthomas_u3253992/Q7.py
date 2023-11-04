"""
               University of Canberra
        Programming for Data Science G (11521) - 2022 (S2)
                    Assignment 3

Question 7 [4 marks] (Scikit-learn): Use the program in Week 11 Tutorial for Scikit-learn.
Implement function get_confusion_matrix below that inputs y_pred, y_test and class labels, and outputs the confusion
matrix. The function should work with any number of class labels. Note the numbers in y_pred and y_test are class label
indices.

Please use Pandas package to implement the function and do not use other packages.
       import pandas as pd
       #############################################
       def get_confusion_matrix(true_list, predicted_list, class_labels):
           # Add your code here. Only Pandas package is imported
           return #confusion matrix
       #############################################
Use the program in Week 11 Tutorial that uses Scikit-learn (Page 6) with to test this function.
Remove the following code from that program

#Plot confusion matrix
   metrics.plot_confusion_matrix(classifier, X_test, y_test,
   display_labels=class_names)
   plt.show()
and add the following code
   labels = ['Setosa', 'Versicolour', 'Virginica']
   confusion_matrix = get_confusion_matrix(y_pred, y_test, labels)
   print(confusion_matrix)
then add the get_confusion_matrix function you implemented.
The program with correct function implementation will output the following:
            Setosa  Versicolour  Virginica
Setosa           13        0        0
Versicolour       0        15       0
Virginica         0         1       9

FAQs:
Only pandas-specific code can be used within `get_confusion_matrix' function

Marking rubric:
    Correctly generating confusion matrix data frame 2 marks
    Generating expected output                       2 marks
"""

import pandas as pd


def get_confusion_matrix(true_list, predicted_list, class_labels):
    # Add your code here. Only Pandas package is imported
    
    # creating confusion matrix using pandas crosstab function
    # reference: https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html
    confusion_matrix = pd.crosstab(true_list, predicted_list)
    
    # updates the row labels
    confusion_matrix.index = class_labels
    
    # updates the column labels
    confusion_matrix.columns = class_labels
    
    return confusion_matrix

## Original code
# metrics.plot_confusion_matrix(classifier, X_test, y_test, display_labels=class_names)
# plt.show()


# from week 11 code 

# actual values
y_test = [2, 1, 0, 2, 0, 2, 0, 1, 1, 1, 2, 1, 1, 1, 1, 0, 1, 1, 0, 0, 2, 1, 0, 0, 2, 0, 0, 1, 1, 0, 2, 1, 0, 2, 2, 1, 0, 1]

# predicted values
y_pred = [2, 1, 0, 2, 0, 2, 0, 1, 1, 1, 2, 1, 1, 1, 1, 0, 1, 1, 0, 0, 2, 1, 0, 0, 2, 0, 0, 1, 1, 0, 2, 1, 0, 2, 2, 1, 0, 2]

# class labels
labels = ['Setosa', 'Versicolour', 'Virginica']

confusion_matrix = get_confusion_matrix(y_pred, y_test, labels)
print(confusion_matrix)
