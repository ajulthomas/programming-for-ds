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

# function to write data to file
def write_list_to_file(file_path, data_list):
    f = None
    try:
        # open file in write mode
        f = open(file_path, 'w')
        
        # each item in list
        for item in data_list:
            # write to file
            f.write(item)
            
    # capture the exception, if any
    except Exception as ex:
        # print exception
        print(ex.args)
    finally:
        if f:
            f.close() # close file
