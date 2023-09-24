 #########################################################################################
#																						#
# 								PROGRAMMING IN DATA SCIENCE		                        #
#								ASSIGNMENT-1 b										    #
#								STUDENT ID: u3253992								    #
#								STUDENT NAME: AJUL THOMAS							    #
#								DATE OF SUBMISSION: 24-09-2023                          #
#								UNDER GRADUATE OR POST GRADUATE: POST GRADUATE          #
#																						#
##########################################################################################

import io_module as io
import clustering as cluster
import tkinter as tk

# creates a window
window = tk.Tk()

# sets the window title
window.title('Programming for Data Science - Assignment -1')

# width x height + x_offset + y_offset:
window.geometry("1920x1080")

# configure the rows
window.rowconfigure(3, minsize=10, weight=1) #3 rows

# configure columns
window.columnconfigure(2, minsize=50, weight=1) #2 columns

# application variables
app_font = "Arial, 12"
myfont = "Arial, 16"

# global varaibales
dimension = tk.IntVar()
file_selected = None
cluster_size = tk.IntVar()
cluster_centers = []
clustered_data = []

# dimensions to be plotted; 
# important for multidimensional data
xi = tk.IntVar()
xi.set(0)


yi = tk.IntVar()
yi.set(1)

# dimension list to select from
xi_list = [0, 1]
yi_list = [0, 1]

# add left side Frame
left_frame = tk.Frame(master=window, width=320, height=1080, bg="lightgrey")
left_frame.grid(row=1, column=0, sticky="w")

# add Canvas
canvas = tk.Canvas(window, bg="white", width=1600, height=1080)
canvas.grid(row=1, column=1, sticky="nswe")

# add main Label
lbl_header = tk.Label(text="K Means Clustering", font=myfont, height=1)
lbl_header.grid(row=0, column=0, columnspan=2)


# function to compose file name based on user selections
def selectItem():
   global file_selected
   global xi_list
   global yi_list
   global xi_choose
   global yi_choose
   global xi
   global yi
   # checks if both user inputs are available
   if(cluster_size.get() and dimension.get()):
       # creates file name from user inputs
       file_selected = f'datasets/data_{cluster_size.get()}c_{dimension.get()}d.txt'
       
       # updates the text in selected file tkinter label
       selected_file.config(text=file_selected)
       
       # update the corordinates dropdown list
       xi_list = [x for x in range(dimension.get())]
       yi_list = [y for y in range(dimension.get())]
       
       # clear the current drop down menu options
       xi_choose['menu'].delete(0, 'end')
       yi_choose['menu'].delete(0, 'end')
       
       # for each item in updated list
       for i in xi_list:
           # update the x co-rdinate options
           # reference: chatGPT AI
           xi_choose['menu'].add_command(label=i, command=lambda value=i: xi.set(value))
           
           # update the y-cordinate options
           # reference: chatGPT AI
           yi_choose['menu'].add_command(label=i, command=lambda value=i: yi.set(value))
           
       # set initial values as selected options
       xi.set(xi_list[0])
       yi.set(yi_list[1])
## end of function
        
## add radiobutton to get the cluster size of the data to be read
# label for the radio button
lbl_cluster_size = tk.Label(master=left_frame, text="Select the cluster size: ", 
                            bg="lightgrey", font=app_font)
lbl_cluster_size.place(x=10,y=10)


c2 = tk.Radiobutton(master=left_frame, text="2 clusters", value=2, variable=cluster_size,
                    bg="lightgrey", font=app_font, command=selectItem)
c2.place(x=10, y=40)

c4 =  tk.Radiobutton(master=left_frame, text="4 clusters", value=4, variable=cluster_size,
                     bg="lightgrey", font=app_font, command=selectItem)
c4.place(x=130, y=40)


## add Radiobutton to get dimensions of data 
lbl_dimension = tk.Label(master=left_frame, text="Select the dimensions: ", 
                            bg="lightgrey", font=app_font)
lbl_dimension.place(x=10, y=80)

ry = tk.Radiobutton(master=left_frame, text="2 dimensions", variable=dimension, value=2, 
                    command=selectItem, bg="lightgrey", font=app_font)
rn = tk.Radiobutton(master=left_frame, text="4 dimensions", variable=dimension, value=4, 
                    command=selectItem, bg="lightgrey", font=app_font)
ry.place(x=10, y=100)
rn.place(x=130, y=100)


## labels to show the file used on user input parameters
lbl_file_selected = tk.Label(master=left_frame, text="File selected:", 
                            bg="lightgrey", font=app_font)
lbl_file_selected.place(x=10, y=140)

selected_file = tk.Label(master=left_frame, text="", fg="navy", anchor="w", width=25, 
                         height=1, font=app_font, bg="lightgrey")
selected_file.place(x=10, y=160)


## choose dimensions to plot, drop-down menu to choose coordinates to plot on 2D plane
lbl_choose_dim = tk.Label(master=left_frame, text="Choose the dimensions to plot:",
                            bg="lightgrey", font=app_font)
lbl_choose_dim.place(x=10, y=200)

# dropdown_menus_reference: https://www.geeksforgeeks.org/dropdown-menus-tkinter/
xi_choose_lbl = tk.Label(master=left_frame, text="x:", bg="lightgrey", font=app_font)
xi_choose_lbl.place(x=10, y=230)

xi_choose = tk.OptionMenu(left_frame, xi, *xi_list)
xi_choose.place(x=40, y=230)

yi_choose_lbl = tk.Label(master=left_frame, text="y:", bg="lightgrey", font=app_font)
yi_choose_lbl.place(x=10, y=270)

# dropdown_menus_reference: https://www.geeksforgeeks.org/dropdown-menus-tkinter/
yi_choose = tk.OptionMenu(left_frame, yi, *yi_list)
yi_choose.place(x=40, y=270)

# button to run the k-means clustering algorithm on the selected data file
button = tk.Button(master=left_frame, text="Run", fg="black", bg="lightblue", 
                   width=15, height=1, font=app_font)
button.place(x=10, y=500)

# defines the handle click function which initiates the clustering using k-means algorithm
def handle_click(event):
    global cluster_centers
    global clustered_data
    if(file_selected and cluster_size and dimension):
        
        # reads dataset
        read_data = io.read_multi_dim_data(file_selected)
        
        # get the cluster centers and list of clustered data 
        (cluster_centers, clustered_data) = cluster.k_means_cluster(cluster_size.get(), read_data)
        
        # print(cluster_centers)
        # print(clustered_data)
        
        # plots the results to canves
        plot_results()
        
# binds the handle click function to run button
button.bind("<Button-1>", handle_click)

# transform the points so that they are visible on the screen
# basically scales and translates given point
def transform_point(x,y):
    # scale factor to scale each point
    s=100
    
    # horizontal translation factor to translate each point along x axis 
    tx=250
    
    # vertical translation factor: translates each point along y axis
    ty=250
    return (x*s + tx, y*s + ty)
    

# plot the graph
def plot_point(x,y, outline="red", fill="red"):
    global canvas
    
    # radius to plot a point
    r=2
    
    # transforming each point so that it is visible on the canvas
    (x, y) = transform_point(x, y)
    
    # plotting the point
    canvas.create_oval(x-r, y-r, x+r, y+r, outline=outline, fill=fill)
    
# draw line between two points
def draw_line(x1, y1, x2, y2, fill="black"):
    # refer the global canvas varaiable
    global canvas
    
    # transform point1 to be seen on canvas 
    (x1,y1) = transform_point(x1, y1)
    
    # tranform point to be seen on canvas
    (x2,y2) = transform_point(x2, y2)
    
    # creates a line
    canvas.create_line(x1, y1, x2, y2, fill=fill)


def plot_results():
    global cluster_centers
    global clustered_data
    global xi, yi
    colors = ["red", 'lavender',"blue", "green", "skyblue"]
    
    canvas.delete('all')
    
    for i in range(len(cluster_centers)):
        
        # select the current cluster enter
        cluster_center = cluster_centers[i]
        
        # coordinates of the cluster_center to be plotted
        (cx, cy) = (cluster_center[xi.get()], cluster_center[yi.get()])
        
        # plot the cluster center
        plot_point(cx, cy, outline="black", fill="black")
        
        # samples that belongs to the current cluster_center
        samples = clustered_data[i]
            
        print(f'plotting cluster {i} with cluster center {cluster_center} with {len(samples)} samples in it.')
        
        for sample in samples:
            # coordinates of the sample
            (sx, sy) = (sample[xi.get()], sample[yi.get()])
            
            # plotting sample point
            plot_point(sx, sy, outline=colors[i], fill=colors[i])
            
            # draw line
            draw_line(cx, cy, sx, sy, fill="gray50")

# starts eventloop on the window
window.mainloop()

