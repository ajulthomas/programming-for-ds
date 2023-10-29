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
    
    datasets = ['Iris', 'Breast Cancer', 'Wine Quality']
    algorithms = ['KNN', 'SVM']
    
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
    gscv_classifier = GridSearchCV(model, param_grid, cv=cv, scoring="accuracy", n_jobs= -1, refit=True)
    
    # fit the model
    gscv_classifier.fit(X_train, y_train)
    
    # predict the results
    y_pred = gscv_classifier.predict(X_test)
    
    # test prediction data
    test_pred = pd.DataFrame({ 'test': y_test, 'pred': y_pred })
    # print(test_pred.T.to_string(header=False))
    
    # print accuracy score
    accuracy = metrics.accuracy_score(y_test, y_pred) * 100
    # print(accuracy)
    
    # print confusion matrix
    cm = metrics.confusion_matrix(y_test, y_pred)
    # print(cm)
    
    cm_visualize = metrics.ConfusionMatrixDisplay(cm, display_labels= dataset.target_names)
    
    # print GridSearchCV results 
    gscv_results = gscv_classifier.cv_results_
    gscv_results = pd.DataFrame(gscv_results)
    # print(gscv_results.columns)
    # print(type(gscv_results))
    # print(gscv_results[['params']])
    
    if (chosen_algorithm == 0):
        gscv_results = gscv_results[['param_n_neighbors','mean_test_score', 'std_test_score']]
    else:
        gscv_results = gscv_results[['param_C', 'param_gamma', 'param_kernel', 'mean_test_score', 'std_test_score']]

    
    # return a dictionary of results and outcomes of the trained model
    results = {
        'dataset': f'{datasets[chosen_dataset]}',
        'classifier': f'{algorithms[chosen_algorithm]}',
        'kfold': cv,
        'obs': X.shape[1],
        'features': X.shape[0],
        'classes': f'{dataset.target_names}',
        'accuracy': accuracy,
        'best_params': gscv_classifier.best_params_,
        'best_model': gscv_classifier.best_estimator_,
        'best_score': gscv_classifier.best_score_,
        'results': gscv_results,
        'cm': cm,
        'cmd': cm_visualize,
        'cfr': metrics.classification_report(y_test, y_pred, target_names=dataset.target_names),
        'test_pred': test_pred
        }
    print_results_to_console(results)
    
    return results
    ## end of function
    

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
            'C': [0.1, 1, 10, 100],
            'gamma':[0.000000001, 0.00000001, 0.0000001, 0.000001,0.00001, 0.0001, 0.001, 0.01, 0.1, 1.0],
            'kernel': ['rbf']
            }
        return (SVC(), param_grid)
## end of function


def print_results_to_console(results):
    print('=============================================================================================')
    print('{0:^100s}'.format("Assignment 2 - Classification in Data Science"))
    print('=============================================================================================\n')
    # print('--------------------------------------------------------------')
    print(f'Chosen dataset: {results["dataset"]} Dataset')
    print(f'Chosen Algorithm: {results["classifier"]} Classifiier')
    print(f'K-fold value: {results["kfold"]}')
    print('\n')
    
    print(f'The dataset contains {results["features"]} features and {results["obs"]} observations')
    print(f'Target classes: {results["classes"]}')
    print('\n')
    
    print(f'Model accuracy: {results["accuracy"]}')
    print('\n')
    
    # confusion matrix 
    print('Confusion matrix:')
    print('-------------------\n')
    print(results['cm'])
    print('\n')
    
    # print results hyper parameter tuning
    print('Results from fine tuneing the model:')
    print('-------------------\n')
    print(f'Best parameters: {results["best_params"]}')
    print(f'Best Model: {results["best_model"]}')
    print(f'Best Score: {results["best_score"]}')
    print('\n')
    
    # classification report 
    print('Classification report:')
    print('------------------------\n')
    print(results['cfr'])
    print('\n')
    
    # cross validation results
    print('Cross validation results:')
    print('--------------------------\n')
    print(results['results'].to_string(index=False))
    print('\n')
    
    # testing data and predicted data
    print('Test Data and Model Predictions : ')
    print('-----------------------------------\n')
    print(results['test_pred'].T.to_string(header=False))
    
    print('\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--END--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')