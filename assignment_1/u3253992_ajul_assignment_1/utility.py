import tkinter as tk

## function to initiate classsification
def knn_classify(unknown_dataset, red_dataset, blue_dataset):
    red_samples_text = []
    blue_samples_text = []
    for sample in unknown_dataset:
        nearest_red = find_nearest_neighbour(sample, red_dataset)
        nearest_blue = find_nearest_neighbour(sample, blue_dataset)
        nearest_class = ''
        if(nearest_red.get("distance") > nearest_blue.get("distance")):
            blue_samples_text.append(f'{sample} blue\n')
            nearest_class='blue'
        else:
            red_samples_text.append(f'{sample} red\n')
            nearest_class='red'
        print(f"The unknown point {sample} falls in {nearest_class} class")
    return red_samples_text + blue_samples_text
# end function


###function to calculate distance
def calculate_distance(point1, point2):
    distance = 0
    ##write your code here.
    for i in range(len(point1)):
        distance += (point2[i] - point1[i]) * (point2[i] - point1[i])
        distance = distance**0.5
    return distance
#end function


#define function
def find_nearest_neighbour(unknown_sample, data_list):
    shortest_distance = calculate_distance(unknown_sample, data_list[0])
    nearest_sample = () #tuple
    for sample in data_list:
        dist = calculate_distance(unknown_sample, sample)
        if shortest_distance > dist:
            shortest_distance = dist
            nearest_sample = sample
    return { "nearest_sample": nearest_sample, "distance": shortest_distance }
#end function

