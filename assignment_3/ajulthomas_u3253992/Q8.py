"""
               University of Canberra
        Programming for Data Science G (11521) - 2022 (S2)
                    Assignment 3

Question 8 [4 marks] (Tkinter): Implement a graphical user interface (GUI) program using Tkinter
with the following tasks:
• The GUI window only has a frame (left) and a canvas (right).
• The frame contains a dropdown list or a group of 3 radio buttons.
• User can select a data file from a dropdown list or from a group of 3 radio buttons displayed
on the frame.
• After a data file is selected, the program will immediately display all data samples in that
data file on the canvas. No button is required.
• The data files are blue_2d.txt, red_2d.txt and unknown_2d.txt used in Assignment 1. Any
colour and shape can be used to display data samples.
It is acceptable if your program can work with 2 dimensional data only.

FAQs: Pls check Assignment 1

Marking rubric:
    Creating the expected GUI window                 2 marks
    Plotting data points                             2 marks

"""

# Your code here



import tkinter as tk

# creates a window
window = tk.Tk()

# sets the window title
window.title('Programming for Data Science - Assignment -3')

# width x height + x_offset + y_offset:
window.geometry("1920x1080")

# configure the rows
window.rowconfigure(3, minsize=10, weight=1) #3 rows

# configure columns
window.columnconfigure(2, minsize=50, weight=1) #2 columns

# application variables
app_font = "Arial, 12"
myfont = "Arial, 16"

# add left side Frame
left_frame = tk.Frame(master=window, width=320, height=1080, bg="lightgrey")
left_frame.grid(row=1, column=0, sticky="w")

# add Canvas
canvas = tk.Canvas(window, bg="white", width=1600, height=1080)
canvas.grid(row=1, column=1, sticky="nswe")

# add main Label
lbl_header = tk.Label(text="Question 8", font=myfont, height=1)
lbl_header.grid(row=0, column=0, columnspan=2)


file_selected = tk.IntVar()
files = ['blue_2d.txt','red_2d.txt', 'unknown_2d.txt']

#Function to read multi-dimension data from a file
def read_multi_dim_data(filename):
    """
    Reads a multi-dimensional data from a file.
    """
    dataset =[]

    ##from tutorial
    f = None
    try:
        # open the file in read mode
        f = open(filename, 'r')
        while True:
            # read each line and store it to varaible line
            line = f.readline()
            
            # if length of line is zero, i.e end of file, break out of the loop
            if len(line) == 0: #end of file
                break
            
            # replace the new line character from the data that's read from file
            line = line.replace('\n', '') #remove end of line \n character
            
            #use split function to separate x & y strings then
            coordinate_string = line.split(' ') #x y coordinates in string format 
            
            #use float function to convert coordinate string to numbers 
            coordinates = [ float(x) for x in coordinate_string ]
            
            # create a tuple of coordinates
            coordinate_tuple = tuple(coordinates)
            
            #add them as a tuple (x, y) to dataset that is a list
            dataset.append(coordinate_tuple)
            
    except Exception as ex:
        print(ex.args)
    finally:
        if f:
            f.close() # close the file

    return dataset
### END OF FUNCTION


# function to scale and translate point 
def transform_point(x,y):
    # scale factor to scale each point
    s=100
    
    # horizontal translation factor to translate each point along x axis 
    tx=250
    
    # vertical translation factor: translates each point along y axis
    ty=250
    return (x*s + tx, y*s + ty)
### END OF FUNCTION


# plot the graph
def plot_point(x,y, outline="red", fill="red"):
    global canvas
    
    # radius to plot a point
    r=4
    
    # transforming each point so that it is visible on the canvas
    (x, y) = transform_point(x, y)
    
    # plotting the point
    canvas.create_oval(x-r, y-r, x+r, y+r, outline=outline, fill=fill)
### END OF FUNCTION


# plot the data
def plot_data(samples):
    global file_selected
    
    # defines the array of colours
    colors = ['blue', 'red', 'black']
    
    # selelct the colour to plot
    c = colors[file_selected.get()]
    
    # for each sample
    for sample in samples:
        # coordinates of the sample
        (sx, sy) = (sample[0], sample[1])
        
        # plotting sample point
        plot_point(sx, sy, outline=c, fill=c)
### END OF FUNCTION    
    

#Function to handle user input
def selectItem():
    global file_selected
    global select_item_calls
    
    # clear the canvas
    canvas.delete('all')
    
    # prepares the file path
    selected_file_path = f'Files4A3/{files[file_selected.get()]}'
    
    # updates the label to notify the selected file
    selected_file_lbl.config(text=f'Plots data points from file {files[file_selected.get()]}')
    
    # reads dataset
    read_data = read_multi_dim_data(selected_file_path)
    
    # plots the data
    plot_data(read_data)
### END OF FUNCTION

## add radiobutton to enable the file selection 
# label for the radio button
lbl_select_file = tk.Label(master=left_frame, text="Select the file to plot: ", 
                            bg="lightgrey", font=app_font)
lbl_select_file.place(x=10,y=10)


f1 = tk.Radiobutton(master=left_frame, text="blue_2d.txt", value=0, variable=file_selected,
                    bg="lightgrey", font=app_font, command=selectItem)
f1.place(x=10, y=40)

f2 =  tk.Radiobutton(master=left_frame, text="red_2d.txt", value=1, variable=file_selected,
                     bg="lightgrey", font=app_font, command=selectItem)
f2.place(x=10, y=80)

f3 =  tk.Radiobutton(master=left_frame, text="unknown_2d.txt", value=2, variable=file_selected,
                     bg="lightgrey", font=app_font, command=selectItem)
f3.place(x=10, y=120)


# label to notify the current file selected for plotting
selected_file_lbl = tk.Label(master=left_frame, text="", fg="navy", anchor="w", font=app_font, bg="lightgrey")
selected_file_lbl.place(x=10, y=160)

# calls select item for the first time
selectItem()

# starts eventloop on the window
window.mainloop()



