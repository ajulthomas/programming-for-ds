#-------------------------------------------------------------------------------------
# Unit Code      : 11521 Sem2                                                 #
# Unit Name      : Programming in Data Science                                #
# Student Id     : u3247467                                                   #
# Student Name   : Radhey Gawand                                              #
# Course         : Post Graduate                                              #
# Submission Date: 30/10/2022                                                 #
#
#--------------------------------------------------------------------------------------

# importing the required libaraires
import os
import tkinter as tk
from tkinter import PhotoImage, messagebox
from tkinter.constants import BOTH, YES
import machinelearning_module as classification

model_data = {} # creating empty dictonary
screen = tk.Tk() # main window
screen.title("Assignement 2") #Title of the window

screen.geometry("1330x820+300+100") # set window size
screen.rowconfigure(3, minsize=10, weight=1)  # 3 rows
screen.columnconfigure(2, minsize=50, weight=1) # 2 cols

# Selecting font and adding header
s_font = "Verdana, 14"
s_header = tk.Label(text="Classification Alogrithm", font=s_font, height=1, fg="navy")
s_header.grid(row = 0, column = 0, columnspan = 2)

# Creating aframe
s_frame = tk.Frame(master=screen, width=350, height=500, bg="white smoke")
s_frame.grid(row=1, column=0, sticky="W")

# creating widget to display visual components
s_widget = tk.Canvas(screen, bg="white", width=980, height=500)
s_widget.grid(row=1, column=1, sticky="NSEW")

#label for displaying charts for confusion matrix
pic_label1 = tk.Label(s_widget, bg="white")
pic_label1.place(x=2,y=2)

create_label = tk.Label(s_widget, width=1, height=500).place(x=470, y=2)

#label for displaying charts cv or knn plot matrix
pic_label2 = tk.Label(s_widget, bg="white")
pic_label2.place(x=490,y=2)

# label to show class name and its number
showl_class = tk.Label(screen, fg="navy", font=s_font, anchor="nw")
showl_class.place(x=15, y=530)

# label to show best parameter
showl_param = tk.Label(screen, fg="navy", font=s_font, anchor="nw")
showl_param.place(x=15, y=570)

#Label to show the accuracy of the model
showl_accuracy = tk.Label(screen, fg="navy", font=s_font, anchor="nw")
showl_accuracy.place(x=15, y=630)

#Label to display prediction score
showl_pred = tk.Label(screen, fg="navy", anchor="nw", font=s_font, justify="left")
showl_pred.place(x=530, y=530)

#Label to display test score
showl_tests = tk.Label(screen, fg="navy", anchor="nw", font=s_font, justify="left")
showl_tests.place(x=530, y=660)


# --------------------
# Creating the UI of the required Radio buttons
# --------------------


# label for data
select_dataset = tk.Label(master=s_frame, text="Choose Data: ",
                          fg="mediumblue", anchor="w", width=25, height=1, font=s_font,
                          bg="white smoke")
select_dataset.place(x=10, y=10) # position of the Label - Select Dataset

show_dataset = tk.Label(master=s_frame, text="", fg="green", anchor="w", width=25, 
                         height=1, font=s_font, bg="white smoke")


df_data = tk.StringVar()  
df_data.set(' ') 

# function showing the dataset selected by user
def select_df():
    output = str(df_data.get()) + " dataset selected." 
    show_dataset.config(text=output)
    
    
#button for the Breast cancer dataset 
button_breastcancer = tk.Radiobutton(master=s_frame, text="Breast Cancer Data",
                                   variable=df_data, command=select_df,
                                   value="Breast Cancer", bg="white smoke", font=s_font)
button_breastcancer.place(x=15, y=40)


# button for the Iris dataset
button_Iris = tk.Radiobutton(master=s_frame, text="Iris Data", value="Iris",
                           variable=df_data, command=select_df,
                           bg="white smoke", font=s_font)
button_Iris.place(x=15, y=70)

# button for the Wine dataset
button_Wine = tk.Radiobutton(master=s_frame, text="Wine Data", value="Wine",
                           variable=df_data, command=select_df,
                           bg="white smoke", font=s_font)
button_Wine.place(x=15, y=100)

show_dataset.place(x=15, y=130) 

# -----------------------------------------------------------------------------
# Show the  'Select Classifier' label along with  the two radio button used by 
# the user to select the classifiers name
# -----------------------------------------------------

# Label for Classifier
selectl_classifier = tk.Label(master=s_frame, text="Choose Classifier: ",
                                fg="mediumblue", anchor="w", width=25, height=1, font=s_font,
                                bg="white smoke")
selectl_classifier.place(x=10, y=180)

showl_classifier = tk.Label(master=s_frame, text="", fg="green", anchor="w", width=25, 
                         height=1, font=s_font, bg="white smoke")

df_classifier = tk.StringVar()  # define a string variable
df_classifier.set(' ')

# this function will show the classifier select by the user
def selectedClassifier():
    classifier_op = str(df_classifier.get()) + " classifier selected." 
    showl_classifier.config(text=classifier_op)
    
# button for knn
button_KNN = tk.Radiobutton(master=s_frame, text="KNN",
                          variable=df_classifier,
                          command=select_df,
                          value="KNN", bg="white smoke", font=s_font)
button_KNN.place(x=15, y=210)

# button for SVM 
button_SVM = tk.Radiobutton(master=s_frame, text="SVM",
                          variable=df_classifier,
                          command=select_df,
                          value="SVM", bg="white smoke", font=s_font)
button_SVM.place(x=15, y=240)

showl_classifier.place(x=15, y=270) 

#Label for Choose no of K Folds
selectl_Kfold = tk.Label(master=s_frame, text="Choose no of K Folds: ",
                                fg="mediumblue", anchor="w", width=25, height=1, font=s_font,
                                bg="white smoke")
selectl_Kfold.place(x=10, y=320) # position of the Label - Select K fold

# add Label - for showing the selected K fold
showl_kfold = tk.Label(master=s_frame, text="", fg="green", anchor="w", width=25, 
                         height=1, font=s_font, bg="white smoke")

# Dropdown menu of Kfold
Kfold_values = [
    "3",
    "5",
    "7",
    "9",
    "11",
    "13",
    "15"
    ]

st_K = tk.StringVar()
st_K.set(' ') 


def nokfold(number):
    choice = "Selected K fold value : " + str(st_K.get())
    showl_kfold.config(text=choice)
    
kfold_menu = tk.OptionMenu(s_frame, st_K, *Kfold_values, command=nokfold)
kfold_menu.place(x=200, y=320)

showl_kfold.place(x=15, y=350)


# The function will run the algorithm based on the data and classifier ap per user slection
def machine_learn():
    # The required elements data,classifier ,kfold stored in variables
    user_dataset = df_data.get()
    user_classifier = df_classifier.get()
    user_kfold = st_K.get()
    
    # validation rules
    issue_alert = "Can Not Run Program!!! \n"
    issue_alert += "\n Please select the following: \n"
    counter = 0
    
    # Loop to check if user has selected data clasierfier and kfold
    # if not slected error message gets diplayed
    if user_dataset == " ":
        counter += 1
        issue_alert += "\n" + str(counter) +  ". Select Data \n"
    
    if user_classifier == " ":
        counter += 1
        issue_alert += "\n" + str(counter) +  ". Select Classifier \n"
    
    if user_kfold == " ":
        counter += 1
        issue_alert += "\n" + str(counter) +  ". Select K-Fold \n"
        
    if user_dataset != " " and user_classifier != " " and user_kfold != " ":
        
        # This will run classification module in based on the 3 variables provided by the user
        ml_data = classification.select_model(user_dataset,user_classifier, user_kfold)
        
        # get path of the file i.e. th directory 
        dir_name = os.path.dirname(__file__)
        
        #Confusion Matrix plot is saved in img1
        save_pic1 = "fig1.png" #path of the image
        file_loc1 = os.path.join(dir_name, save_pic1)
        
        #New obeject that the confusion matrix image is being creatd to display it on the GUi window
        Confusion_matrix_pic = PhotoImage(file=file_loc1)
        
        
        pic_label1.image = Confusion_matrix_pic
        pic_label1.configure(image=Confusion_matrix_pic)
        
        #The 2nd plot is saved in the img2 file path
        save_pic2 = "fig2.png" 
        file_loc2 = os.path.join(dir_name, save_pic2)
        
        pic2 = PhotoImage(file = file_loc2)
        
        pic_label2.image = pic2
        pic_label2.configure(image=pic2)
        
        
        ###################
        #The below print statements print the required information that will be displayed on the window screen
        print('----------------------------------------------------------------')
        print('Dataset is : ', user_dataset)
        print('Classifier is : ', user_classifier)
        print('K-fold value is :', user_kfold)
        
        print('\n Number of samples: ', ml_data['sample_values'])
        print('\n Dimensionality (features): ', ml_data['features_values'])
        
        print('\n Array of class names:', ml_data['classvalues'])
        print('\n Number of classes:', len(ml_data['classvalues']))
        
        print("\n Confusion Matrix: ")
        print(ml_data['Confusion_Matrix_resu'])
       
        print("\n y prediction: ") 
        print(ml_data['y_pred_resu'])
        
        print("\n y test: ")
        print(ml_data['ytest_v'])
        
        print("\n Grid scores on validation set: \n")
        
        for mean, std, param in zip(ml_data['mean_resu'], ml_data['stds_resu'], ml_data['result_resu']):
            print("\t Parameter: %r, accuracy: %0.3f (+/-%0.03f)" % (param, mean, std*2))
        
        print("\n Best parameter:", ml_data['best_params_resu'])
        
        print("\n Accuracy: {0:.2f}%".format(ml_data['accuracy_resu']))
        print('----------------------------------------------------------------')
        
        # On gui diplay array class namesl
        showl_class.config(text="Array of class names: " + str(ml_data['classvalues']))
        
        # display the best paramters
        showl_param.config(text="\n Best parameter: " + str(ml_data['best_params_resu']))
        
        # Display the accuracy of the ml model
        showl_accuracy.config(text="\n Accuracy: {0:.2f}%".format(ml_data['accuracy_resu']))

        # display the prediction value of the model
        showl_pred.config(text="y prediction: \n" + str(ml_data['y_pred_resu']))
        
        # display the test value of model
        showl_tests.config(text="\n y test: \n" + str(ml_data['ytest_v'])) 
    else:
       
        messagebox.showwarning("Warning", issue_alert)
        screen.focus_force()


#GUI of the run button
Run_button = tk.Button(master=s_frame, text="Run", fg="green",
                   bg="lightblue", width=10, height=1, font=s_font,
                   command=machine_learn)
Run_button.place(x=30, y=400)

def test_again():
    df_data.set(' ')
    show_dataset.config(text="")
    
    df_classifier.set(' ')
    showl_classifier.config(text="")
    
    st_K.set(' ')
    showl_kfold.config(text="")
    
    pic_label1.config(image="")
    pic_label2.config(image="")
    
    showl_class.config(text="")
    showl_param.config(text="")
    showl_accuracy.config(text="")
    showl_pred.config(text="")
    showl_tests.config(text="")


# Gui of the Reset button
Reset_button = tk.Button(master=s_frame, text="Reset", fg="navy",
                     bg="lightblue", width=10, height=1, font=s_font,
                     command=test_again)
Reset_button.place(x=190, y=400)

# Function to exit the code
def close_ml():
    screen.destroy()  


#GUI of the  Exit button  
Exit_button = tk.Button(master=s_frame, text=" Exit Program ", height=1,
                    width=15, font=s_font, bg="lightblue", fg="red",
                    command=close_ml)
Exit_button.place(x=80, y=450)

# display the tkinter screen
screen.mainloop()