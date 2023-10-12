import io_data_module as iodata
import tkinter

data_list = iodata.read_multi_dim_data('datasets/data_4c_2d.txt')

window = tkinter.Tk()
cvs_width = 800
cvs_height = 600
canvas = tkinter.Canvas(window, bg="white", height=cvs_height, width=cvs_width)

#Display data 
r = 4 #radius
ix = 0 #index of value in a data sample for x 
iy = 1 #index of value in a data sample for y 

#(sx, sy, tx, ty) = iodata.transform_data_for_canvas_display(data_list, idx=ix, idy=iy, canvas_height=cvs_height, canvas_width=cvs_width)
(sx, sy, tx, ty) = iodata.get_canvas_scaling(data_list, ix, iy, cvs_height, cvs_width)
#(sx,sy,tx,ty) = iodata.get_canvas_scaling(data_list)

#Show data list
iodata.display_data(data_list, ix, iy, 'red', 'circle', canvas, r, sx, sy, tx, ty)

canvas.pack()
window.mainloop()
