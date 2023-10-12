#Function to transform data to display on canvas
def transform_data_for_canvas_display(data_list, idx=0, idy=1, canvas_width=800, canvas_height=600):
    #data_list is a list of nD samples, n > 2
    maxW = -1E8 #max width
    minW = 1E8  # min width
    maxH = -1E8  # max height
    minH = 1E8  # min height
    for sample in data_list: 
        if maxW < sample[idx]:
            maxW = sample[idx]
        if minW > sample[idx]:
            minW = sample[idx]
        if maxH < sample[idy]:
            maxH = sample[idy]
        if minH > sample[idy]:
            minH = sample[idy]
    sx = canvas_width / (maxW - minW)
    tx = canvas_width * minW / (minW - maxW) 
    sy = canvas_height / (maxH - minH) 
    ty = canvas_height * minH  / (minH - maxH) 
    return (sx, sy, tx, ty)


#Function to display lines on canvas
def display_lines(centre, data_list, xi=0, yi=1, colour='red', canvas=None, sx=150, sy=150, tx=300, ty=200):
    for sample in data_list:
        x = sample[xi]*sx + tx
        y = sample[yi]*sy + ty
        x2 = centre[xi]*sx + tx
        y2 = centre[yi]*sy + ty
        if canvas != None:
            canvas.create_line(x, y, x2, y2, fill = colour)
#end of function


#Function to display shapes on canvas
def display_data(data_list, xi=0, yi=1, colour='red', shape='circle', canvas=None, r=5, sx=150, sy=150, tx=300, ty=200):
    for sample in data_list:
        x = sample[xi]
        y = sample[yi]
        x = x*sx + tx 
        y = y*sy + ty
        if canvas != None:
            if shape == 'circle':
                canvas.create_oval(x-r, y-r, x+r, y+r, outline = colour, fill=colour)
            elif shape == 'square':
                canvas.create_rectangle(x-r, y-r, x+r, y+r, outline=colour, fill=colour)
            elif shape == 'triangle':
                canvas.create_polygon(x, y-r, x-r, y+r, x+r, y+r, outline=colour, fill=colour)
            else: #if input shape is unknown, draw circle
                canvas.create_oval(x-r, y-r, x+r, y+r, outline = colour, fill=colour)
#end of function


# NOTE SteveD: using defaults can lead to the wrong data being used.  Safer not to use at all.
# def get_canvas_scaling(data_list, idx=0, idy=1, canvas_height=600, canvas_width=800):
def get_canvas_scaling(data_list, idx, idy, canvas_height, canvas_width):
    '''  Calculates a scaling factor and x y offset to allow all data points to be drawn on a given canvas '''

    extents = find_extents(data_list)

    # choose the max and min value for each of the dimensions (idx and idy) to be plotted.
    xmin, xmax = extents[idx]
    sfx = canvas_width/(xmax-xmin)
    ymin, ymax = extents[idy]
    sfy = canvas_height/(ymax-ymin)

    # Preserve Aspect ration by choosing the smaller scale
    sf = min(sfx, sfy)*0.8

    # calc offsets to centre of canvas (first term/2) then move the offset back to the canvas origin (xmin*sf)
    # NOTE: origion (0,0) is at the top left corner of the canvas ( or frame or widget ), so Y increaes left to right, X increases top to bottom.
    xo = (canvas_width -(xmax-xmin)*sf)/2 - xmin * sf
    yo = (canvas_height-(ymax-ymin)*sf)/2 - ymin * sf

    return (sf, sf, xo, yo)


def find_extents(data_list):
    """  Finds min and max value for each dimension in a DimN data list 
         Returns a list of (min, max) per dimension"""

    min_dim = list(data_list[0])
    max_dim = list(data_list[0])

    for data in data_list:
        for i in range(len(data)):
            if min_dim[i] > data[i]:
                min_dim[i] = data[i]
            elif max_dim[i] < data[i]:
                max_dim[i] = data[i]

    for data in data_list:
        for i in range(len(data)):
            if min_dim[i] > data[i]:
                min_dim[i] = data[i]
            elif max_dim[i] < data[i]:
                max_dim[i] = data[i]

    # transpose the result so it is more usable
    ext = []
    for i in range(len(min_dim)):
        ext.append((min_dim[i], max_dim[i]))

    return (ext)


#########  Other stuff not that interesting

def read_multi_dim_data(filename, separator=' ', label=''):
    ''' Reads csv multi-dim data from a text file and returns as a list of tuples '''

    dataset = [] #dataset is a python list 
    f = None
    try:
        f = open(filename, 'r')
        while True:
            line = f.readline()
            if len(line) == 0: #end of file
                break
            line = line.replace('\n', '')
            if len(line) == 0: #blank line
                continue
            row = list( line.split(separator) )
            for i in range(len(row)):
                try: # to convert to a float
                    row[i] = float(row[i])
                except:
                    row.pop(i)
            if label != '':
                row.append(label)
            dataset.append(tuple(row))
    except Exception as ex:
        print(ex.args)
    finally:
        if f:
            f.close()
    return dataset


def distance(p1, p2):
    """ Calculates the distance between two n-dimension points (p1 p2) in two tuples.
    Parameters: 
        p1 = ( Dim1, Dim2, Dim3....DimN )
        p2 = ( Dim1, Dim2, Dim3....DimN ) 
    Returns: Distance"""

    d = 0
    for i in range(len(p1)):
        d += (p2[i] - p1[i]) * (p2[i] - p1[i])
    d = d ** 0.5
    return d


def find_nearest_neighbour(sample, data_list):
    '''  Find nearest point in a data set to a sample point   '''

    nearest_data = data_list[0]
    d_min = distance(sample, data_list[0])
    for data in data_list:
        d = distance(sample, data)
        if d < d_min:
            d_min = d
            nearest_data = data

    return nearest_data
