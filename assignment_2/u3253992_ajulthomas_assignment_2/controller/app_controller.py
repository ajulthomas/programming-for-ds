# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 14:39:20 2023

@author: ajult
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import models
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# load required libraries
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import datasets, metrics, mixture


# starting point of the modelling process
def create_ml_model(chosen_dataset, chosen_algorithm, cv=5):
    
    # get the right dataset
    dataset = get_chosen_dataset(chosen_dataset)
    
    # get the right model
    (model, param_grid) = get_chosen_model(chosen_algorithm)
    
    # dataset features
    X = dataset.data
    
    # dataset target
    y = dataset.target
    
    # split data into train and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state= 17)
    
    # load grid search cross validation
    gscv_classifier = GridSearchCV(model, param_grid, cv=cv, scoring="accuracy", n_jobs= -1, verbose=1, refit=True)
    
    # fit the model
    gscv_classifier.fit(X_train, y_train)
    
    # predict the results
    y_pred = gscv_classifier.predict(X_test)
    
    # print accuracy score
    accuracy = metrics.accuracy_score(y_test, y_pred) * 100
    print(accuracy)
    
    # print confusion matrix
    cm = metrics.confusion_matrix(y_test, y_pred)
    print(cm)
    
    cm_visualize = metrics.ConfusionMatrixDisplay(cm, display_labels= dataset.target_names)
    
    # print GridSearchCV results 
    gscv_results = gscv_classifier.cv_results_
    gscv_results = pd.DataFrame(gscv_results)
    # print(gscv_results.columns)
    # print(type(gscv_results))
    print(gscv_results[['params']])
    
    if (chosen_algorithm == 0):
        gscv_results = gscv_results[['param_n_neighbors','mean_test_score']]
    else:
        gscv_results = gscv_results[['param_C', 'param_gamma', 'param_kernel', 'mean_test_score']]
        
        
    # return a dictionary of results and outcomes of the trained model
    
    return {
        'accuracy': accuracy,
        'best_params': gscv_classifier.best_params_,
        'best_model': gscv_classifier.best_estimator_,
        'results': gscv_results,
        'confusion_matrix': cm_visualize
        }
    
    # visualize confusion matrix
    
    # plot the cross validation results
    
    

# function to get the dataset chosen by the user
# cd = 0, Iris Dataset
# cd = 1, Breast Cancer Dataset
# cd = 2, Wine Quality Dataset
def get_chosen_dataset(cd):
    if(cd == 0):
        return datasets.load_iris()
    elif(cd == 1):
        return datasets.load_breast_cancer()
    else:
        return datasets.load_wine()

# function to instantiate the classification algorithm chosen by user.
# ca = 0, KNN classifier
# ca = 1, SVC classifier
def get_chosen_model(ca):
    if(ca == 0):
        param_grid = {'n_neighbors': range(1,31) }
        return (KNeighborsClassifier(), param_grid)
    else:
        param_grid = {
            'C': [0.1,1, 10, 100],
            'gamma':[0.000000001, 0.00000001, 0.0000001, 0.000001,0.00001, 0.0001, 0.001, 0.01, 0.1, 1.0],
            'kernel': ['rbf']
            }
        return (SVC(), param_grid)

