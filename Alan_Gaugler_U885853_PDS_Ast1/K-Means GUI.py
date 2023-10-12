# Import tkinter and all functions from the function module
import Data_Module_GUI as iodata
import tkinter as tk
from tkinter import END

############################## Run the validate_input ###############################################
def run_main():
    # Because this function requires input from GUI widgets and displays information on the GUI,
    # it could not be placed in the IO module.

    # The purpose of the main function is to validate all the input files from the GUI. If there are any issues,
    # the user will be asked to correct them. Once all the valid files have been loaded, the datasets will be passed to
    # the K_means_classifier function in the iomodule and the results will be returned and plotted by calling the
    # create_K_Means_plot function to be plotted in the canvas which is also in the GUI.

    # If a previous plot had been made, it will be cleared before calculating the new cluster points.
    # and all information in the TextOutputs
    C.delete('all')
    save_txt.delete(0, END)
    save_status.set("")
    status.set("")
    status2.set("")
    status3.set("")
    status4.set("")
    status4_txt = ""

    ######## Section: Input a valid filename and load the input file #################
    # Read the radio button assignment.
    option = int(var1.get())
    print(f'option: {option}')
    # From the radio buttons, the mentioned file will be loaded. This is a shortcut to save typing.
    # If Option 5 is selected, the filename typed in the file_txt Entry widget will be entered.
    if option == 1:
        ip_file = 'data_2c_2d.txt'
    elif option == 2:
        ip_file = 'data_2c_4d.txt'
    elif option == 3:
        ip_file = 'data_4c_2d.txt'
    elif option == 4:
        ip_file = 'data_4c_4d.txt'
    elif option == 5:
        ip_file = file_txt.get()

    # The filename has been selected and now the file will be loaded.
    status_text = f"File Status: \n"
    # The function read_file in the iodata module is called to load the file.
    file_ = iodata.read_file(ip_file)
    
    # If the file is not empty, the appropriate variables will be assigned.
    if file_[0] != []:
        # File loaded successfully. Status is updated.
        # The input dataset is obtained and its status will be displayed.
        # As was requested in the assignment, the data sample (named 'dataset' below) is stored as a tuple.
        dataset = file_[0]
        print(f'Dataset: {dataset}')
        status_text += f'{file_[1]}\n'
        # append True if file loaded successfully
        valid_file = file_[2]
        # The number of dimensions of the dataset are determined.
        dimensions = len(dataset[0])
        # Determine the number of samples in the dataset
        data_samples = len(dataset)
    # If there was an issue with loading the file, else will be executed.
    else:
        # File was either empty or did not load. Status is updated.
        status_text += f'{file_[1]}\n'
        # The various variables are updated.
        dataset = file_[0]
        # append False if file could not be loaded
        valid_file = file_[2]
        dimensions = "N/A"
        data_samples = "N/A"

    # The status of loading the file is updated in the GUI
    status_text = status_text.rstrip()
    status2_text = f'Number of dimensions:   {dimensions}\n' \
                    f'Number of samples in dataset: {data_samples}'

    ######## Section: Input a valid value for K #################
    # A valid integer greater than 1 must be entered for the number of clusters.
    try:
        clust_num = int(clust_txt.get())
        if clust_num <=1:
            status_text += f'\nERROR! Number of clusters must be > 1'
            valid_k = False
        else:
            # If valid, the status will be updated.
            status_text += f'\nNumber of clusters entered: {clust_num}'
            status2_text += f'\nNumber of clusters: {clust_num}'
            valid_k = True
    # If not a valid integer, an exception will be raised ad the status is updated.
    except ValueError:
        status_text += "\nERROR! Enter a valid integer: K >= 2"
        valid_k = False
    except TypeError:
        status_text += "\nERROR! Enter a valid integer: K >= 2"
        valid_k = False

    ######## Section: Input a valid convergence tolerance #################
    # A valid float must be entered for the convergence tolerance.
    try:
        conv_tol = float(conv_txt.get())
        if conv_tol > 0:
            status_text += f'\nConvergance Tolerance: {conv_tol}'
            status2_text += f'\nConvergance Tolerance: {conv_tol}'
            valid_conv_tol = True
        else:
            status_text += "\nERROR! Conv Tol must be > 0."
            valid_conv_tol = False
    except ValueError:
        status_text += "\nERROR! Enter a valid number for Conv Tol."
        valid_conv_tol = False
    except TypeError:
        status_text += "\nERROR! Enter a valid number for Conv Tol."
        valid_conv_tol = False
        
    ######## Section: Input a valid Number of Iterations #################
    # A valid integer greater than 1 must be entered for the number of iterations.
    try:
        num_iter = int(iter_txt.get())
        if num_iter <=1:
            status_text += f'\nERROR! Number of iterations must be > 1'
            valid_iter = False
        else:
            status_text += f'\nNumber of iterations entered: {num_iter}'
            status2_text += f'\nNumber of iterations: {num_iter}'
            valid_iter = True
    except ValueError:
        status_text += "\nERROR! Enter a valid integer for iterations: K >= 2"
        valid_iter = False
    except TypeError:
        status_text += "\nERROR! Enter a valid integer for iterations: K >= 2"
        valid_iter = False

    # The status of entering the correct input is updated and displayed.
    # If there are issues, the user can read the display and correct the input.
    status.set(status_text)
    status2.set(status2_text)

    # Only if all inputs were correct can the program continue to call the K_means_classifier algorithm.
    cont = False
    if valid_file and valid_k and valid_conv_tol and valid_iter:
        cont = True
        status3.set("All entries are valid\nDetermining clusters.")
    else:
        status3.set("There are invalid input entries.\nPlease correct them before continuing.")
        status4_txt = 'Correct Errors In Above Displays Before Continuing!'
        status4.set(status4_txt)

    # If everything is OK, the program will proceed.
    if cont:
        # The input entered in the GUI and the dimensions are passed onto the K_means_classifier function in the iodata module.
        results = iodata.K_means_classifier(dataset, clust_num, conv_tol, num_iter)
        
        # The required information is returned to be able to create the plot and save the required output to file.
        # It is unpacked from the returned tuple.

        # As was requested in the assignment, the final cluster allocations of the data points is a list of tuples.
        # list_of_best_fit is a list containing tuples.
        # Each tuple is a tuple of datapoints belonging to each cluster (corresponding to the index of the tuple).
        # Each of those tuples contain the coordinates of each data point of all dimensions.
        list_of_best_fit = results[0]
        print(f'list of best fit: {list_of_best_fit}')
        # As was requested, best_centroids is a list of tuples, where each tuple contains the coordinates of all
        # dimensions for each centroid or cluster centre point.
        best_centroids = results[1]
        print(f'Best Centroids: {best_centroids}')
        zde_calls = results[2]
        conv_cnt = results[3]
        min_itr = results[4]
        min_sse = results[5]
        global output_text
        output_text = results[6]

        # The plot in the canvas window of the GUI will now be created, by calling the create_plot function.
        iodata.create_K_Means_plot(C, list_of_best_fit, best_centroids, clust_num)

        # Some information on the results of the K-means algorithm are updated on the GUI
        status3_text = f'K-Means Cluster Classifier completed\n' \
                       f'Number of Random Point Resets: {zde_calls}\n' \
                       f'Number of Convergances: {conv_cnt}\n'
        # If the algorithm never converged, more iterations needs to be run to give it a greater chance of converging.
        if conv_cnt == 0:
            status3_text += 'Increase number of iterations or reduce K\n'

        status3_text += f'Minimum SSE of all points to their closest centroid: {round(min_sse, 3)}\n' \
                        f'Best iteration: {min_itr}'
        # Display the status in the GUI
        status3.set(status3_text)

######################################### End of Run the main program ####################################################
############################### Save File Function #####################################################################
# When the Save File button is clicked, the program will save the output as a text file.

# As this function requires input from GUI widgets and displays information on the GUI, it could not be placed in the IO module.
# However the required parameters are passed onto the write_file function in the IO module where file is actually saved.

def save_file():
    # Retrieve file name from GUI filename Entry widget.
    op_file = save_txt.get()
    # Call the write_file function from the Data Module to save the file in the working directory.
    save_status_text = iodata.write_file(op_file, output_text)
    # Display the status of saving the file
    save_status.set(save_status_text)

######################### Main GUI Program using Tkinter #############################################################
# The GUI window is set up in tkinter.
# This is the main program that runs GUI and structures its display. When the user enters data and clicks buttons
# this program will call the appropriate functions and it also receives display information
# from other approrpiate parts of the program.

window = tk.Tk()
window.title('Programming for Data Science. Assignment 1, Question 2')
# width x height + x_offset + y_offset:
window.geometry("1200x770-200-50")

# Configure a window of 3 rows and 2 columns
window.rowconfigure(3, minsize=10, weight=1) #2 rows
window.columnconfigure(2, minsize=50, weight=1) #2 columns

# define various font settings
f1 = "Arial, 11"
f2 = "Arial 12 bold"
f3 = "Arial 11 bold"

# Create and arrange frames.
frame_1 = tk.Frame(master=window, width=300, height=30, bg="silver", relief="sunken")
frame_1.grid(row=0, column=0, columnspan=2, sticky="nswe")

frame_2 = tk.Frame(master=window, width=1200, height=120, bg="silver", relief="sunken")
frame_2.grid(row=1, column=0, columnspan=2, sticky="nswe")

left_frame = tk.Frame(master=window, width=350, height=420, bg="lightgrey")
left_frame.grid(row=2, column=0, sticky="nswe")

# Create the canvas for the plots.
C = tk.Canvas(window, bg="lightblue", width=620, height=620)
C.grid(row=2, column=1, sticky="nswe")

# Set up the label header
lbl_header = tk.Label(master = frame_1, text="K Means Clustering Program", font=f2, height=1, width = 120,
                      relief="groove", bg='silver')
lbl_header.place(x=0, y=0)

########################################## Status Window #############################################
# All display widgets in Frame 2 are set up
status = tk.StringVar()
status_lbl = tk.Label(master=frame_2, textvariable=status, relief="sunken", bg='white', font=('arial', 12))
status_lbl.place(x=10, y=1)

status2 = tk.StringVar()
status_lbl2 = tk.Label(master=frame_2, textvariable=status2, relief="sunken", bg='white', font=('arial', 12))
status_lbl2.place(x=480, y=1)

status3 = tk.StringVar()
status_lbl3 = tk.Label(master=frame_2, textvariable=status3, relief="sunken", bg='white', font=('arial', 12))
status_lbl3.place(x=750, y=1)

########################################## Input Window ##############################################################
# All input and display widgets are set up in the left panel.

# Certain variables for widget positioning adjustment on the GUI are defined.
x1 = 10
y0 = 5
gap1 = 22
gap2 = 28

# All input widgets are labelled and positioned in the left panel.
status4 = tk.StringVar()
status_lbl4 = tk.Label(master=left_frame, textvariable=status4, relief="sunken", fg='red', bg='white', font=f2)
status_lbl4.place(x=x1, y=y0)

# Appropriately adjust the vertical spacing of the widgets below the previous one.
y1 = y0 + gap2

lbl_1 = tk.Label(master=left_frame, text="Either enter files manually or select ",
                    fg="black", anchor="w", width=35, height=1, font=f1, bg="lightgrey")
lbl_1.place(x=x1, y=y1)

# Appropriately adjust the vertical spacing of the widgets below the previous one.
y2 = y1 + gap1
lbl_2 = tk.Label(master=left_frame, text="assignment files with predefined dimensions: ",
                    fg="black", anchor="w", width=35, height=1, font=f1, bg="lightgrey")
lbl_2.place(x=10, y=y2)

var1 = tk.IntVar()
var1.set(5)

y3 = y2 + gap1
y4 = y3 + gap1
y5 = y4 + gap1
y6 = y5 + gap1
y7 = y6 + gap1

r1 = tk.Radiobutton(master=left_frame, text="data_2c_2d.txt", variable=var1, value=1,
                    bg="lightgrey", font=f1)
r2 = tk.Radiobutton(master=left_frame, text="data_2c_4d.txt", variable=var1, value=2,
                    bg="lightgrey", font=f1)
r3 = tk.Radiobutton(master=left_frame, text="data_4c_2d.txt", variable=var1, value=3,
                    bg="lightgrey", font=f1)
r4 = tk.Radiobutton(master=left_frame, text="data_4c_4d.txt", variable=var1, value=4,
                    bg="lightgrey", font=f1)
r5 = tk.Radiobutton(master=left_frame, text="Enter manually", variable=var1, value=5,
                    bg="lightgrey", font=f1)
r1.place(x=10, y=y3)
r2.place(x=10, y=y4)
r3.place(x=10, y=y5)
r4.place(x=10, y=y6)
r5.place(x=10, y=y7)

# Appropriately adjust the vertical spacing of the widgets below the previous one.
y8 = y7 + gap2
y9 = y8 + gap1
y10 = y9 + gap1
y11 = y10 + gap2
y12 = y11 + gap1
y13 = y12 + gap2
y14 = y13 + gap1
y15 = y14 + gap2
y16 = y15 + gap1
y17 = y16 + gap1
y18 = y17 + gap1

# Setup the labels and text entries.
man_lbl = tk.Label(master=left_frame, text='If manual, ensure "Enter manually" is selected above,',
                    fg="black", anchor="w", width=42, height=1, font=f3, bg="lightgrey")
man_lbl.place(x=10, y=y8)

file_lbl = tk.Label(master=left_frame, text="Place file in working directory and enter file name:",
                    fg="black", anchor="w", width=42, height=1, font=f3, bg="lightgrey")
file_lbl.place(x=10, y=y9)
file_txt = tk.Entry(master=left_frame, fg="black", width=35, font=f1)
file_txt.place(x=10, y=y10)

clust_lbl = tk.Label(master=left_frame, text="Enter the number of clusters: (K>1): ",
                   fg="black", anchor="w", width=40, height=1, font=f1, bg="lightgrey")
clust_lbl.place(x=10, y=y11)
clust_txt = tk.Entry(master=left_frame, fg="black", width=35, font=f1)
clust_txt.place(x=10, y=y12)

conv_lbl = tk.Label(master=left_frame, text="Enter the Convergence Tolerance. Typical: 0.0001.",
                       fg="black", anchor="w", width=40, height=1, font=f1, bg="lightgrey")
conv_lbl.place(x=10, y=y13)
conv_txt = tk.Entry(master=left_frame, fg="black", width=35, font=f1)
conv_txt.insert(0, "0.0001")
conv_txt.place(x=10, y=y14)

iter_lbl = tk.Label(master=left_frame, text="Enter the number of Iterations. Typical: 100.",
                       fg="black", anchor="w", width=40, height=1, font=f1, bg="lightgrey")
iter_lbl.place(x=10, y=y15)
iter_lbl2 = tk.Label(master=left_frame, text="More may be required if K is large:",
                       fg="black", anchor="w", width=30, height=1, font=f1, bg="lightgrey")
iter_lbl2.place(x=10, y=y16)
iter_txt = tk.Entry(master=left_frame, fg="black", width=35, font=f1)
iter_txt.insert(0, "100")
iter_txt.place(x=10, y=y17)

####################################### Create the Executional Buttons ###############################################
# The Run and Quit buttons are created.
# The Run button will execute to run "run_main" function when pressed which calculates the nearest neigbour classifier
# and plots the results.

y18 = y17 + gap2
run_button = tk.Button(master=left_frame, text="Run", fg="black", bg="silver", width=7, height=1, font=f3,
                      relief="raised", command=run_main)
run_button.place(x=10, y=y18)

# The Quit button will close the GUI and the program
quit_button = tk.Button(master=left_frame, text="Quit", fg="black", bg="silver", width=7, height=1, font=f3,
                        relief="raised", command=window.destroy)
quit_button.place(x=100, y=y18)

# The Save File widgets are created in the left panel.
# Appropriately adjust the vertical spacing of this widget below the previous one.
y19 = y18 + gap2 + 10
y20 = y19 + gap1
save_lbl = tk.Label(master=left_frame, text="Enter filename to save file",
                    fg="black", anchor="w", width=35, height=1, font=f1, bg="lightgrey")
save_lbl.place(x=10, y=y19)

save_txt = tk.Entry(master=left_frame, fg="black", relief="sunken", width=35, font=f1)
save_txt.place(x=10, y=y20)

y21 = y20 + gap2
save_button = tk.Button(master=left_frame, text="Save File", fg="black", bg="silver", width=10, height=1, font=f3,
                      relief="raised", command=save_file)
save_button.place(x=10, y=y21)

y22 = y21 + gap2 + 7
save_status = tk.StringVar()
save_status_lbl = tk.Label(master=left_frame, textvariable=save_status, relief="sunken", bg='white', font=('arial', 12))
save_status_lbl.place(x=10, y=y22)

# This executes the mainloop of the tkinter GUI.
window.mainloop()
