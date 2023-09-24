import tkinter as tk

## function to initiate classsification
def knn_classify(unknown_dataset, red_dataset, blue_dataset):
    # list to store the unknown samples classified as red
    red_samples_text = []
    
    # list to store unknown samples classified as blue
    blue_samples_text = []
    
    # loop through each unknown sample
    for sample in unknown_dataset:
        
        # the dictionary containing coordinates of nearest red sample and distance
        nearest_red = find_nearest_neighbour(sample, red_dataset)
        
        # the dictionary containing coordinates of nearest blue sample and distance
        nearest_blue = find_nearest_neighbour(sample, blue_dataset)
        
        # initialising the nearest class of the current unknown sample as an empty string
        nearest_class = ''
        
        # comparing the distance to the nearest red sample and nearest blue sample
        if(nearest_red.get("distance") > nearest_blue.get("distance")):
            # appending the results
            blue_samples_text.append(f'{sample} blue\n')
            # if nearest blue point is closest, the unknown point is categorized as blue
            nearest_class='blue'
        else:
            # appending the results
            red_samples_text.append(f'{sample} red\n')
            # if nearest red point is closest, the unknown point is categorized as red
            nearest_class='red'
        print(f"The unknown point {sample} falls in {nearest_class} class")
    
    # appending the results and returning them
    return red_samples_text + blue_samples_text
# end function


###function to calculate distance
def calculate_distance(point1, point2):
    # initialising the distance variable
    distance = 0
    
    # looping through each co-ordinate of the point 1 and calculates the distnace between the points
    for i in range(len(point1)):
        # add the square of difference between one coordinate
        distance += (point2[i] - point1[i]) * (point2[i] - point1[i])
        
    # taking the square root of the distance variable 
    distance = distance**0.5
    
    # returns the distance
    return distance
#end function


#define function
def find_nearest_neighbour(unknown_sample, data_list):
    # initialising the shortest distance
    shortest_distance = calculate_distance(unknown_sample, data_list[0])
    
    # initialise the nearest sample as an empty tuple
    nearest_sample = () #tuple
    
    # iterate for each sample in the data_list
    for sample in data_list:
        # calculates distance between the two given points
        dist = calculate_distance(unknown_sample, sample)
        
        # if the new distance is less than the shortest distance
        if shortest_distance > dist:
            # set new distance as shortest distance
            shortest_distance = dist
            # update nearest sample as the current sample
            nearest_sample = sample
            
    # returns a dictionary with nearest sample and distance to it
    return { "nearest_sample": nearest_sample, "distance": shortest_distance }
#end function

