# Import tkinter and all functions from the function module
import Data_Module_GUI as iodata
import tkinter as tk
from tkinter import END

########################################### run_main function ############################################################
def run_main():
    # Because this function requires input from GUI widgets and displays information on the GUI, 
    # it could not be placed in the IO module.
    
    # The purpose of the main function is to validate all the input files from the GUI. If there are any issues,
    # the user will be asked to correct them. Once all the valid files have been loaded, the datasets will be passed to
    # the nearest_neighbour_classifier function in the iomodule and the results will be returned to be displayed in the GUI
    # and plotted in the canvas which is also in the GUI.

    # If a previous plot had been made, it will be cleared before calculating the new cluster points.
    # All information in the TextOutputs will also be cleared.
    C.delete('all')
    save_txt.delete(0, END)
    save_status.set("")
    status.set("")
    status2.set("")
    status3.set("")
    status4.set("")
    # status text for two displays will be initiated.
    status_text = f"File Status: \n"
    status4_txt = ""

    # Read the radio button assignment.
    dim = int(var1.get())

    # From the radio buttons, a value that is not 1 means that the program will load the assignment files
    # for the selected dimension. This is a shortcut to save typing in the file names.
    # They can be manually entered in if the radio button','s variable is set to 1.
    if dim != 1:
        # If "Enter manually" is not set, all filenames in the Entry widgets will be cleared to avoid confusion.
        red_txt.delete(0, END)
        blue_txt.delete(0, END)
        unknown_txt.delete(0, END)

        # Load the appropriate files for chosen dimension.
        # files return a tuple of predetermined file names.
        file_list = iodata.get_file_names(dim)
        print()
        print(f'files are {file_list}')

        red_name = file_list[0]
        blue_name = file_list[1]
        unknown_name = file_list[2]

    # If the radio button was set to "enter manually", the entered file names will be loaded and used to
    # classify the points of the unknown file. If there is a problem with the files, the error will be displayed in
    # the GUI and the files can be re-entered and run again.
    else: # This option is executed if files were entered manually.
        # The three filenames are read from the text entry widgets.
        red_name = red_txt.get()
        blue_name = blue_txt.get()
        unknown_name = unknown_txt.get()
        file_list = [red_name, blue_name, unknown_name]
        print(f'file_list: {file_list}')

    # Once the three filenames are stored in a list, the iodata function get file status will be called.
    # It will form a loop to call another function to load each list individually and report back it's loading status
    # as well as the data list.
    load_results = iodata.get_file_status(file_list, status_text)

    # Lists are created to store the information from loading the files.
    status_text = load_results[0]
    data_lists = load_results[1]
    dim_list = load_results[2]
    valid_file = load_results[3]

    # The data points are placed into the three data lists.
    # It was requested in the assignment that each data sample is a tuple and they are stored in three lists of
    # red, blue and unknown. This has been done as is shown below.
    red_data = data_lists[0]
    blue_data = data_lists[1]
    unknown_data = data_lists[2]
    print(f'red_data: {red_data}')
    print(f'blue_data: {blue_data}')
    print(f'unknown_data: {unknown_data}')

    # If at least one of the loaded files had an issue, the program cannot execute.
    # The flag file_issues is set to False.
    if False in valid_file:
        file_issues = True
    else:
        file_issues = False

    # The status of loading the files is displayed in the first widget on the top.
    status_text = status_text.rstrip()
    status.set(status_text)

    # The number of dimensions for each loaded file is displayed.
    dim_status2 = f'Number of dimensions:\n{red_name}: {dim_list[0]}\n' \
                  f'{blue_name}: {dim_list[1]}\n{unknown_name}: {dim_list[2]}'

    status2.set(dim_status2)

    # Determine if the dimensions of the three files are the same.
    # If they are not, the flag dim_issues is set to True.
    dim_issues = False
    if (dim_list[0] != dim_list[1]) or (dim_list[0] != dim_list[2]):
        dim_issues = True

    # if there are no issues with the files and their dimensions the continue flag is set to True and the program
    # can continue to run the nearest neighbour algorithm.
    if (not file_issues) and (not dim_issues):
        status3_txt = f'Continuing \n No errors with input files.'
        cont = True
    else:
        # If there are issues detected, the continue flag is set to False and the program will wait until
        # new files have been successfully loaded
        status3_txt = 'The following errors have been found:\n'
        if file_issues:
            status3_txt += 'Issues loading a valid file.\n'
        if dim_issues:
            status3_txt += 'Files have inconsistent dimensions\n'
        cont = False
        status4_txt = 'Correct Errors In Above Displays Before Continuing!'

    # Display the status of running the program.
    status3_txt = status3_txt.rstrip()
    status3.set(status3_txt)
    status4.set(status4_txt)

    # If there are no issues with the files, the program will continue and pass the datasets as arguments into the
    # nearest_neighbour_classifier algorithm
    # points in the unknown file using the nearest neighbour classifier algorithm.
    if cont == True:
        names_list = [red_name, blue_name, unknown_name]
        results = iodata.nearest_neighbour_classifier(red_data, blue_data, unknown_data)

        # The reformatted datapoints and output text strings are returned from the nearest_neighbour_classifier function
        # and are unpacked from the tuple. They can now be used to plot the results and save the data to an output file.
        red_points = results[0][0]
        blue_points = results[0][1]
        known_points = results[0][2]
        lines_list = results[1]
        global output_text
        output_text = results[2]
        global output_text_2
        output_text_2 = results[3]

        plot_list = [red_points, blue_points, known_points]
        print()

        # Call the function to plot the data points.
        iodata.create_NNC_plot(C, plot_list, lines_list)

        # Update the status3 text widget on top to state that the plots have been successfully run.
        status3_txt += "\nNearest Neighbour Classifier has been successfully run.\n" \
                        "The result can be saved as a text file."
        status3.set(status3_txt)

######################################## End of Run Main Function ######################################################
############################################## Save File Function ######################################################
# As this function requires input from GUI widgets and displays information on the GUI, it could not be placed in the IO module.
# When the Save File button is clicked, the program will save the output as a text file.
# However the required parameters are passed onto the write_file function in the IO module where file is actually saved.
# Two formats of output files will be saved.
# The first will have the following format: Unknown Point Index: 0, (0.678713, 0.951598) falls in class: Blue
# The 2nd will end in the extension _2.txt and has the following format: (0.678713, 0.951598) blue
def save_file():
    # Retrieve file name from GUI filename Entry widget.
    op_file = save_txt.get()
    # Call the write_file function from the Data Module to save the file in the working directory.
    save_status_text = iodata.write_file(op_file, output_text)
    # Add the extension to the 2nd file name and save it.
    op_file_2 = save_txt.get()[:-4] + "_2.txt"
    save_status_text2 = iodata.write_file(op_file_2, output_text_2)
    # Merge the status of saving both files into one text output.
    save_status_text += f'\n{save_status_text2}'
    # Display the status of saving the files
    save_status.set(save_status_text)

##################################### Main GUI Program using Tkinter ####################################################
# The GUI window is set up in tkinter.
# This is the main program that runs GUI and structures its display. When the user enters data and clicks buttons
# this program will call the appropriate functions and it also receives display information 
# from other approrpiate parts of the program.

window = tk.Tk()
window.title('Programming for Data Science. Assignment 1, Question 1')
# width x height.  x_offset + y_offset are not used
window.geometry("1300x760-100-50")

# Configure a window of 3 rows and 2 columns
window.rowconfigure(3, minsize=10, weight=1) #3 rows
window.columnconfigure(2, minsize=50, weight=1) #2 columns

# define various font settings
f1 = "Arial, 11"
f2 = "Arial 12 bold"
f3 = "Arial 11 bold"

# Create and arrange frames.
frame_1 = tk.Frame(master=window, width=1300, height=30, bg="silver", relief="sunken")
frame_1.grid(row=0, column=0, columnspan=2, sticky="nswe")

frame_2 = tk.Frame(master=window, width=1300, height=80, bg="silver", relief="sunken")
frame_2.grid(row=1, column=0, columnspan=2, sticky="nswe")

left_frame = tk.Frame(master=window, width=310, height=450, bg="lightgrey")
left_frame.grid(row=2, column=0, sticky="nswe")

# Create the canvas for the plots.
C = tk.Canvas(window, bg="lightblue", width=710, height=700)
C.grid(row=2, column=1, sticky="nswe")

# Set up the label header
lbl_header = tk.Label(master = frame_1, text="Nearest Neighbour Classifier Program", font=f2, height=1, width = 140,
                      relief="groove", bg='silver')
lbl_header.place(x=0, y=0)

#################################### Status Window #############################################
# All display widgets in Frame 2 are set up
status = tk.StringVar()
status_lbl = tk.Label(master=frame_2, textvariable=status, relief="sunken", bg='white', font=('arial', 12))
status_lbl.place(x=10, y=1)

status2 = tk.StringVar()
status_lbl2 = tk.Label(master=frame_2, textvariable=status2, relief="sunken", bg='white', font=('arial', 12))
status_lbl2.place(x=580, y=1)

status3 = tk.StringVar()
status_lbl3 = tk.Label(master=frame_2, textvariable=status3, relief="sunken", bg='white', font=('arial', 12))
status_lbl3.place(x=820, y=1)

#################################### Input Window ##############################################################
# All input and display widgets are set up in the left panel.

# Certain variables for positioning adjustment are defined.
x1 = 10
y0 = 5
gap1 = 22
gap2 = 35

# All input widgets are labelled and positioned in the left panel.
status4 = tk.StringVar()
status_lbl4 = tk.Label(master=left_frame, textvariable=status4, relief="sunken", fg='red', bg='white', font=f2)
status_lbl4.place(x=x1, y=y0)

# Appropriately adjust the vertical spacing of the widgets below the previous one.
y1 = y0 + gap2

lbl_1 = tk.Label(master=left_frame, text="Either Enter Files Manually: ",
                    fg="black", anchor="w", width=25, height=1, font=f1, bg="lightgrey")
lbl_1.place(x=x1, y=y1)

# Appropriately adjust the vertical spacing of the widgets below the previous one.
y2 = y1 + gap1
lbl_2 = tk.Label(master=left_frame, text="Or Assignment files with predefined dimensions: ",
                    fg="black", anchor="w", width=35, height=1, font=f1, bg="lightgrey")
lbl_2.place(x=10, y=y2)

var1 = tk.IntVar()
var1.set(1)

# Appropriately adjust the vertical spacing of the widgets below the previous one.
y3 = y2 + gap1
y4 = y3 + gap1
y5 = y4 + gap1
y6 = y5 + gap1

r2 = tk.Radiobutton(master=left_frame, text="2 dimensions", variable=var1, value=2,
                    bg="lightgrey", font=f1)
r4 = tk.Radiobutton(master=left_frame, text="4 dimensions", variable=var1, value=4,
                    bg="lightgrey", font=f1)
r8 = tk.Radiobutton(master=left_frame, text="8 dimensions", variable=var1, value=8,
                    bg="lightgrey", font=f1)
rm = tk.Radiobutton(master=left_frame, text="Enter manually", variable=var1, value=1,
                    bg="lightgrey", font=f1)
r2.place(x=10, y=y3)
r4.place(x=10, y=y4)
r8.place(x=10, y=y5)
rm.place(x=10, y=y6)

# Appropriately adjust the vertical spacing of the widgets below the previous one.
y7 = y6 + gap2
y8 = y7 + gap1
y9 = y8 + gap2
y10 = y9 + gap1
y11 = y10 + gap2
y12 = y11 + gap1
y13 = y12 + gap2
y14 = y13 + gap1

man_lbl = tk.Label(master=left_frame, text='If manual, ensure "Enter manually" is selected above.',
                    fg="black", anchor="w", width=42, height=1, font=f3, bg="lightgrey")
man_lbl.place(x=10, y=y7)

man_lbl2 = tk.Label(master=left_frame, text="Place files in working directory and enter file names.",
                    fg="black", anchor="w", width=40, height=1, font=f1, bg="lightgrey")
man_lbl2.place(x=10, y=y8)

red_lbl = tk.Label(master=left_frame, text="Enter Red data file name: ",
                    fg="black", anchor="w", width=25, height=1, font=f1, bg="lightgrey")
red_lbl.place(x=10, y=y9)
red_txt = tk.Entry(master=left_frame, fg="black", width=35, font=f1)
red_txt.place(x=10, y=y10)

blue_lbl = tk.Label(master=left_frame, text="Enter Blue data file name: ",
                   fg="black", anchor="w", width=25, height=1, font=f1, bg="lightgrey")
blue_lbl.place(x=10, y=y11)
blue_txt = tk.Entry(master=left_frame, fg="black", width=35, font=f1)
blue_txt.place(x=10, y=y12)

unknown_lbl = tk.Label(master=left_frame, text="Enter Test (Unlabeled) data file name:",
                       fg="black", anchor="w", width=30, height=1, font=f1, bg="lightgrey")
unknown_lbl.place(x=10, y=y13)
unknown_txt = tk.Entry(master=left_frame, fg="black", width=35, font=f1)
unknown_txt.place(x=10, y=y14)

# The Run and Quit buttons are created.
# The Run button will execute to run "run_main" function when pressed which calculates the nearest neigbour classifier
# and plots the results.
y15 = y14 + gap2
run_button = tk.Button(master=left_frame, text="Run", fg="black", bg="silver", width=7, height=1, font=f3,
                      relief="raised", command=run_main)
run_button.place(x=10, y=y15)

# Pressing the Quit button will close the GUI and end the program.
quit_button = tk.Button(master=left_frame, text="Quit", fg="black", bg="silver", width=7, height=1, font=f3,
                        relief="raised", command=window.destroy)
quit_button.place(x=100, y=y15)

# The Save File widgets are created in the left panel.
# Appropriately adjust the vertical spacing of this widget below the previous one.
y16 = y15 + gap2 + 10

save_lbl = tk.Label(master=left_frame, text="Enter file name to save file",
                    fg="black", anchor="w", width=35, height=1, font=f1, bg="lightgrey")
save_lbl.place(x=10, y=y16)

# Appropriately adjust the vertical spacing of this widget below the previous one.
y17 = y16 + gap1
# The file name will be enetered in this Entry widget.
save_txt = tk.Entry(master=left_frame, fg="black", width=35, font=f1)
save_txt.place(x=10, y=y17)

# Appropriately adjust the vertical spacing of this widget below the previous one.
y18 = y17 + gap2 - 5

# Pressing this button will execute save_file function.
save_button = tk.Button(master=left_frame, text="Save File", fg="black", bg="silver", width=10, height=1, font=f3,
                      relief="raised", command=save_file)
save_button.place(x=10, y=y18)

# Print the status of saving the file.
y19 = y18 + gap2
save_status = tk.StringVar()
save_status_lbl = tk.Label(master=left_frame, textvariable=save_status, relief="sunken", bg='white', font=('arial', 12))
save_status_lbl.place(x=10, y=y19)

# This executes the mainloop of the tkinter GUI.
window.mainloop()
