#Function to read multi-dimension data from a file

def read_multi_dim_data(filename):
    """
    Reads a multi-dimensional data from a file.
    """
    dataset =[]

    ##from tutorial
    f = None
    try:
        f = open(filename, 'r')
        while True:
            line = f.readline()
            if len(line) == 0: #end of file
                break
            
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
            f.close()

    return dataset

# function to write data to file
def write_list_to_file(file_path, data_list):
    f = None
    try:
        f = open(file_path, 'w')
        for item in data_list:
            f.write(item)
    except Exception as ex:
        print(ex.args)
    finally:
        if f:
            f.close()
