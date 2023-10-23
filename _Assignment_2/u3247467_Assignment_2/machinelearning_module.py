from sklearn import datasets, neighbors, metrics, svm
from sklearn.model_selection import train_test_split, GridSearchCV
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""The function will run the based on selection made by the user by using the gui the user will be able to select the following parameters
    
    Arguments/ Parameters used :
    df_name : Dataframe name i.e. "Breast Cancer", "Iris", "Wine"
    model_name : Classification Algorithm on which the model are buils the two models are "KNN" AND "SVM"
    Kfold : K fold value
    
""" 


def select_model(ds_name, model_name, Kfold):
    
    # if else loop is used to load the dataset into ds_name
    if ds_name == "Breast Cancer":
        ds_select = datasets.load_breast_cancer() # Breast cancer dataset is selected
    elif ds_name == "Iris":
        ds_select = datasets.load_iris() # Iris dataset is selected
    elif ds_name == "Wine":
        ds_select = datasets.load_wine() # Wine dataset is selected
    
    # the data represents the predictor variables which will train the model to predict the target variable
    X_predict = ds_select.data 
    
    # samples and features
    n_samples, n_features = X_predict.shape
    
    # the target variable is stored 
    y_target = ds_select.target
    
    # the name of the target variable
    class_names = ds_select.target_names
    
    # Split the dataset into train and test in this case 70 % data is in trainning part(X_train) and 30% in testing part(X_test)
    # After the model is build based on train data we will predict the test data and compare the result with original data
    X_train, X_test, y_train, y_test = train_test_split(X_predict, y_target, test_size = 0.30, random_state = 0)
    
    # Loop is used to select KNN or SVM based on the user selection
    if model_name == "KNN":
        param_range = [{'n_neighbors':range(1,31)}]
        model = neighbors.KNeighborsClassifier()
    elif model_name == "SVM":
        param_range = [{'gamma':[0.000000001, 0.00000001, 0.0000001, 0.000001,0.00001, 0.0001, 0.001, 0.01, 0.1, 1.0]}]
        model = svm.SVC()
        
    #GridSearchCV is a method for looking up the best parameter values from a given grid of parameters.   
    gscv_model = GridSearchCV(
    estimator = model,
    param_grid = param_range,
    cv = int(Kfold),
    scoring = "accuracy")
    
    # TRAINING THE MODEL
    # this function is used to train the data set 
    gscv_model.fit(X_train, y_train)
    
    # Getting the required parameters from the GridSearch CV
    mean_test_score = gscv_model.cv_results_['mean_test_score']
    stds_test_score = gscv_model.cv_results_['std_test_score']
    results = gscv_model.cv_results_['params']
    best_parameter = gscv_model.best_params_
    
    
    # TESTING THE MODEL
    # The trained model will now apply the best values to predict the test data
    y_pred = gscv_model.predict(X_test)
    
    # Plot the confusion matrix to understand how well our model works
    cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
    accuracy = metrics.accuracy_score(y_test,y_pred) * 100
    plotcm = metrics.ConfusionMatrixDisplay(cnf_matrix, display_labels = class_names)
    # plotcm.figure_.set_title('Confusion Matrix Plot')
    plotcm.plot()
    plt.savefig("fig1.png", dpi = 90)
    plt.clf()
    
    # Creating a cross validation plot for KNN
    if model_name == "KNN":
        k_range = range(1,31)
        plt.plot(k_range, gscv_model.cv_results_['mean_test_score'])
        plt.xlabel('Value of K for KNN')
        plt.ylabel('Cross-Validated Accuracy')
        plt.title('Cross Validation plot for KNN')
        plt.savefig('fig2.png', dpi=90)
        plt.clf()
    
     # Creating a cross validation plot for SVM
    if model_name == "SVM":
        C_s = np.logspace(-10,0,10,2)
        plt.semilogx(C_s, np.array(mean_test_score))
        plt.semilogx(C_s, np.array(mean_test_score) + np.array(stds_test_score), 'b--')
        plt.semilogx(C_s, np.array(mean_test_score) - np.array(stds_test_score), 'b--')
        locs, labels = plt.yticks()
        plt.yticks(locs,list(map(lambda x: "%g" % x, locs)))
        plt.ylabel('CV score')
        plt.xlabel('Parameter C')
        plt.title('Cross Validation Plot for SVM')
        plt.savefig("fig2.png",dpi = 80)
        plt.clf()
        
    plt.close("all")
    
    
    # Creating a dictionary and storing all the calculated values
    final_data_dict = dict(
        X_val = X_predict,                  
        y_val = y_target,                  
        features_values = n_features,            
        sample_values = n_samples,             
        classvalues = class_names,          
        Xtrain_v = X_train,             
        Xtest_v = X_test,                
        ytrain_v = y_train,              
        ytest_v = y_test,                
        mean_resu = mean_test_score,               
        stds_resu = stds_test_score,         
        result_resu = results,               
        y_pred_resu = y_pred,                
        best_params_resu = best_parameter,   
        accuracy_resu = accuracy,            
        Confusion_Matrix_resu = cnf_matrix)   
    
    return final_data_dict

