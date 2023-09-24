# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:49:24 2023

@author: ajult
"""

import tkinter as tk
import io_module as io
import k_means_algorithm as cluster

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
xi = 0
yi = 1

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
    # checks if both user inputs are available
    if(cluster_size.get() and dimension.get()):
        file_selected = f'datasets/data_{cluster_size.get()}c_{dimension.get()}d.txt'
        #selected_file.config(text=file_selected)
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

# button to run the k-means clustering algorithm on the selected data file
button = tk.Button(master=left_frame, text="Run", fg="black", bg="red", 
                   width=15, height=1, font=app_font)
button.place(x=10, y=500)

# defines the handle click function which initiates the clustering using k-means algorithm
def handle_click(event):
    global cluster_centers
    global clustered_data
    if(file_selected and cluster_size and dimension):
        print(file_selected)
        read_data = io.read_multi_dim_data(file_selected)
        print(read_data)
        (cluster_centers, clustered_data) = cluster.run_kmeans(cluster_size.get(), read_data)
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
    global canvas
    (x1,y1) = transform_point(x1, y1)
    (x2,y2) = transform_point(x2, y2)
    canvas.create_line(x1, y1, x2, y2, fill=fill)

def plot_results():
    global cluster_centers
    global clustered_data
    global xi, yi
    colors = ["red","blue", "green", "skyblue"]
    
    canvas.delete('all')
    
    for i in range(len(cluster_centers)):
        
        # select the current cluster enter
        cluster_center = cluster_centers[i]
        
        # coordinates of the cluster_center to be plotted
        (cx, cy) = (cluster_center[xi], cluster_center[yi])
        
        # plot the cluster center
        plot_point(cx, cy, outline="black", fill="black")
        
        # samples that belongs to the current cluster_center
        samples = clustered_data[i]
            
        print(f'plotting cluster {i} with cluster center {cluster_center} with {len(samples)} samples in it.')
        
        for sample in samples:
            # coordinates of the sample
            (sx, sy) = (sample[xi], sample[yi])
            
            # plotting sample point
            plot_point(sx, sy, outline=colors[i], fill=colors[i])
            
            # draw line
            draw_line(cx, cy, sx, sy, fill="gray50")

# starts eventloop on the window
window.mainloop()

