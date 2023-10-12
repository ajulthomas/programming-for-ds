import io_data_module as iodata
import tkinter as tk

centre_1 = (5.1, 3.0, 1.1, 0.5)
centre_2 = (4.4, 3.2, 2.8, 0.2)
centre_3 = (5.7, 3.9, 3.9, 0.8)
centre_list = [centre_1, centre_2, centre_3]

data_list = iodata.read_multi_dim_data('datasets/iris.data', separator=',')
print(data_list)

list_1 = []
list_2 = []
list_3 = []

for sample in data_list:
    nearest_centre = iodata.find_nearest_neighbour(sample, centre_list)
    if nearest_centre == centre_1:
        list_1.append(sample)
    elif nearest_centre == centre_2:
        list_2.append(sample)
    else:
        list_3.append(sample)

new_centre_1 = [0,0,0,0]
for index in range(4): #range(len(list_1[0])):
    sum = 0
    for sample in list_1:
        sum += sample[index]
    new_centre_1[index] = sum / len(list_1)
print(new_centre_1)

new_centre_2 = [0,0,0,0]
for index in range(4): #range(len(list_1[0])):
    sum = 0
    for sample in list_2:
        sum += sample[index]
    new_centre_2[index] = sum / len(list_2)
print(new_centre_2)

new_centre_3 = [0,0,0,0]
for index in range(4): #range(len(list_1[0])):
    sum = 0
    for sample in list_3:
        sum += sample[index]
    new_centre_3[index] = sum / len(list_3)
print(new_centre_3)

new_centre_list = [new_centre_1, new_centre_2, new_centre_3]

#Create canvas
window = tk.Tk()
cvs_width = 800
cvs_height = 600
canvas = tk.Canvas(window, bg="white", height=cvs_height, width=cvs_width)

#Display data 
r = 4 #radius
ix = 0 #index of value in a data sample for x 
iy = 1 #index of value in a data sample for y 

(sx,sy,tx,ty) = iodata.get_canvas_scaling(data_list, idx=ix, idy=iy, canvas_height=cvs_height, canvas_width=cvs_width)

lists123 = [list_1, list_2, list_3]

#Show lines 
iodata.display_lines(centre_1, list_1, ix, iy, 'red', canvas, sx, sy, tx, ty)
iodata.display_lines(centre_2, list_2, ix, iy, 'blue', canvas, sx, sy, tx, ty)
iodata.display_lines(centre_3, list_3, ix, iy, 'green', canvas, sx, sy, tx, ty)

#Show data 
iodata.display_data(list_1, ix, iy, 'red', 'circle', canvas, r, sx, sy, tx, ty)
iodata.display_data(list_2, ix, iy, 'blue', 'square', canvas, r, sx, sy, tx, ty)
iodata.display_data(list_3, ix, iy, 'green', 'triangle', canvas, r, sx, sy, tx, ty)

canvas.pack()
window.mainloop()
