# The programs for the Nearest Neighbour Classifier and the K-Means Classifier call functions from this module.
# This module does not have any main programs but rather serves as providing the required functions.
# Some of the functions are shared and used in both programs such as: read_file, write_file and calc_distance.

# Import the required modules.
import tkinter as tk
import random # Ram has approved that the random module can be imported.

############################### Get File Names Function ################################################################
# This function will return the appropriate file names for the number of dimensions added
# in the nearest neighbour classifier program.
# This is a shortcut so that the file names do not have to be typed in.
# The parameter for number of dimensions is passed into the function and the desired filenames are stored as variables.
def get_file_names(dims):
    if dims == 2:
        red_f = "red_2d.txt"
        blue_f = "blue_2d.txt"
        unknown_f = "unknown_2d.txt"
    elif dims == 4:
        red_f = "red_4d.txt"
        blue_f = "blue_4d.txt"
        unknown_f = "unknown_4d.txt"
    elif dims == 8:
        red_f = "red_8d.txt"
        blue_f = "blue_8d.txt"
        unknown_f = "unknown_8d.txt"
    else:
        print("error")
        red_f = ""
        blue_f = ""
        unknown_f = ""
    # A tuple of the filenames is returned to the program.
    return red_f, blue_f, unknown_f
################################# Get File Status ######################################################################

def get_file_status(file_list, status_text):
    # This loop will load the three input files and return a result to the GUI
    # stating if they loaded successfully or not.
    data_lists = []
    dimensions = [0, 0, 0]
    validity = []
    for f in range(len(file_list)):
        ip_file = file_list[f]
        # Calls the read_file function from the io module which returns a tuple containing the dataset, status text
        # of loading the file and a validity flag.
        file_ = read_file(ip_file)
        if file_[0] != []:
            # File loaded successfully. Status is updated.
            data_lists.append(file_[0])
            dimensions[f] = len(data_lists[f][0])
            status_text += f'{file_[1]}\n'
            # append True if file loaded successfully
            validity.append(file_[2])

        else:
            # File was either empty or did not load. Status is updated.
            status_text += f'{file_[1]}\n'
            # append False if file could not be loaded
            validity.append(file_[2])
            data_lists.append(file_[0])

    return(status_text, data_lists, dimensions, validity)

###################################### Read File Function ##############################################################
# This function opens the file, reads the data from it and returns the dataset and other associated information.
def read_file(filename):
    dataset = []  # dataset is a list
    f = None
    # Exception handling. If the file is not found, the program will not crash and the user will be advised there was an issue.
    try:
        f = open(filename, 'r')
        while True:
            # Read one line at a time from the input file.
            line = f.readline()
            if len(line) == 0:  # end of file
                break # If the last line is empty, the end of the file has been reached and the program will leave the while loop.
            line = line.replace('\n', '')  # remove end of line \n character
            coord_pt = line.split(' ')  # x y coordinates in string format are separated by spaces.
            # use split function to separate x & y to n dimensions strings then
            # use float function to convert x & y strings to x & y numbers and
            # add them as a tuple (x, y, ...., n) to dataset that is a list
            data_point = []
            # This loop adds the coordinate for every dimension of a point to a list called data_point
            for idx in range(0,len(coord_pt)):
                data_point.append(float(coord_pt[idx]))
            # The list of coordinates of the point is converted into a tuple
            dp = tuple(data_point)
            # The tuple is then appended to a list of all points in the file.
            dataset.append(dp)
        # After the entire file has been read:
        print(f"{filename} successfully loaded")
        status_text = f"{filename} successfully loaded"
        # The flag of successfully loading the file is set to True.
        valid = True
        # If the file successfully loaded, the dataset, error message and the valid flag set to True are returned.
        return dataset, status_text, valid
    # If there was an error reading the file, an exception will be raised.
    except Exception as ex:
        # The flag of successfully loading the file is set to False.
        valid = False
        print(ex.args)
        if ex.args[0] == 2:
            # if this is true, the file was not found in the working directory.
            status_text = f'"{filename}" was not found. Enter a valid file name.'
            print(f'"{filename}" was not found in the working directory. Enter a valid file name.')
        elif ex.args[0] == "could not convert string to float: 'Nearest'":
            # The file has an invalid format.
            print(f'"{filename}" has an invalid format. Enter a valid file name.')
            status_text = f'"{filename}" has an invalid format. Enter a valid file name.'
        else:
            # An unknown error. This is unlikely to every be executed.
            print(f'{filename}: has an invalid format. Enter a valid file.')
            status_text = f'"{filename}": has an invalid format. Enter a valid file.'
        # If there was an error, an empty dataset, the error message and the valid flag set to False are returned to the main program.
        return [], status_text, valid
    finally:
        if f:
            # In either case, if the file was opened, it will be closed.
            print("File closed")
            f.close()

#################################### Write File Function ###############################################################
# This function will save a file on the hard drive. It takes in the file name and the output data as a text string as
# the input and will write it to a text file in the working directory.
def write_file(op_file, output_text):
    if op_file == '':
        # No file name was entered. The statement in the next line will be returned to the program as a string.
        return "Please enter a valid file name."
    elif op_file.endswith('.txt') != True:
        # In this program a text file must end with the extension ".txt"
        # The statement in the next line will be returned to the program as a string.
        return "Please use extension .txt"
    else:
        # A valid filename has been entered and passed to this function.
        try:
            # The desired filename will be opened and written.
            f = open(op_file, 'x')
            f.write(output_text)
            # After being written, the file will be closed.
            f.close()
            # The statement in the next line will be returned to the program as a string.
            print(f'{op_file} has been stored in the working directory.')
            return (f'{op_file} has been stored.')
        except Exception as ex:
            # If the same filename already exists, an exception will be raised.
            print(ex.args)
            print(f'{op_file} already exists in the working directory.')
            print('Please remove it or choose another name')
            # The statement in the next line will be returned to the program as a string.
            return (f'{op_file} already exists.\n'
                            f'Please remove it or choose another name.')
        except:
            # If another type of error occurs.
            # The statement in the next line will be returned to the program as a string.
            print('Another error occurred')
            return (f'Another error occurred. Try a different filename.')

########################################### Calculate Distance Function ################################################
# This function will calculate and return the euclidian distance between two points of any number of dimensions.
# The input are two data points of equal dimensions.
def calc_distance(p1, p2):
    # Initially the distance is set to 0
    d = 0
    # For every dimension the square of the difference of the points is calculated and added to the total distance d.
    for i in range(len(p1)):
        d += (p2[i] - p1[i])**2
    # After the sum of the square of the difference of the points is calculated for every dimension,
    # the square root of the total is calculated and the result is the actual Euclidian distance between the two points.
    d = d**0.5
    # the distance is returned back to the program that called it.
    return d
########################################################################################################################

# This function will reformat the list of red and blue points into a new list that can be used by the create_NNC_plot function
# in the nearest neighbor classifier program.
def reformat_list(list1, col_fill, col_ol, width, radius):
    new_list = []
    for pts in list1:
        points_info = list()
        points_info.append(pts)
        points_info.append(col_fill)
        points_info.append(col_ol)
        points_info.append(width)
        points_info.append(radius)
        points_info = tuple(points_info)
        new_list.append(points_info)
    return new_list

#######################################################################################################################
# This function will reformat the list of known points into a new list that can be used by the create_NNC_plot function.
def reformat_known_list(k_list, col, width, radius):
    new_list = []
    for pts in k_list:
        points_info = list()
        points_info.append(pts[0])
        points_info.append(pts[1])
        points_info.append(col)
        points_info.append(width)
        points_info.append(radius)
        points_info = tuple(points_info)
        new_list.append(points_info)
    return new_list

###################################### Random Cluster Centres Function #################################################
# For the K-means algorithm, the random cluster starting points will be generated in this function.
# All the data points in the test datasets have all of their points within the range of -2 to 8.
# The random starting points will also fall within this range.
def random_cluster_centres(k_num, dims):
    K_cent = []
    for k in range(k_num):
        random_start_pt = []
        for pt in range(dims):
            random_start_pt.append(random.uniform(-2, 8))
        K_cent.append(random_start_pt)
    return (K_cent)

########################################### Calculate Centroid ########################################################
# This function is called by the K-Means Classifier algorithm also in the IO module.
# It will calculate the new centre of each cluster based on the total distances of each point in the cluster to the centre
# which are averaged. 
def calculate_centroid(cluster_info, cluster_centres, dimensions, K_cent, zde_calls, zero_div_error):
    # The outer loop will loop through all clusters
    for i in range(len(cluster_info)):
        if zero_div_error:
            break
        else:
            # This loop goes through every coordinate (dimension) of the cluster central point and calculates its centre.
            # based on the previously calculated totals and number of points in the cluster.
            for j in range(dimensions):
                try:
                    # The new cluster centre coordinate for each dimension is calculated.
                    cluster_centres[i][j] = cluster_info[i][j+2]/cluster_info[i][1]
                except ZeroDivisionError:
                    # If one cluster did not have any points, then new random cluster points will be chosen.
                    zero_div_error = True
                    zde_calls += 1
                    print("New Zero Division Error: At least one cluster was not the closest to any points.")
                    print("New random start points will be chosen")
                    # if there is a divide by zero, the original cluster point will be left so the program can continue.
                    # However new points will be chosen before the data points are assigned to a cluster again.
                    cluster_centres[i][j] = K_cent[i][j] # was cluster_centres
                    break

    # The updated information of the new cluster centres and associated information is returned to the K-Means Classifier algorithm.
    return cluster_info, cluster_centres, dimensions, K_cent, zde_calls, zero_div_error

######################################## Nearest Neighbor Classifier ###################################################
# This function will receive the red, blue and unknown datasets and calculate which cluster the unknown points
# belong to using a nearest neighbor classifier of k = 1 (only identfying the closest neighbour.
# A tuple is returned with the datasets' lists reformatted for plotting and the output text to be saved in a file.

def nearest_neighbour_classifier(red_data, blue_data, unknown_data):
    print()
    print("continuing")
    # Define an empty list
    known_points = list()
    # Define various output text options.
    output_text_2 = ""
    output_text3 = ""
    output_text = ""

    # This list will be used to plot lines between the unknown point and its closest neighbour.
    lines_list = []

    # This loop will go through all points in the unknown points list and determine its closest point.
    for u_idx in range(len(unknown_data)):
        u_pt = unknown_data[u_idx]

        # Set initial closest (minimum) red point to the first point in the file.
        min_red_idx = 0
        min_red_dist = calc_distance(u_pt, red_data[0])
        # Determine the closest red point by calling the calc_distance function.
        for red_idx in range(len(red_data)):
            red_dist = calc_distance(u_pt, red_data[red_idx])
            if red_dist <= min_red_dist:
                min_red_dist = red_dist
                min_red_idx = red_idx
                min_red_pt = red_data[red_idx]

        # Set initial closest (minimum) blue point to the first point in the file.
        min_blue_idx = 0
        min_blue_dist = calc_distance(u_pt, blue_data[0])
        # Determine the closest blue point
        for blue_idx in range(0, len(blue_data)):
            blue_dist = calc_distance(u_pt, blue_data[blue_idx])
            if blue_dist <= min_blue_dist:
                min_blue_dist = blue_dist
                min_blue_idx = blue_idx
                min_blue_pt = blue_data[blue_idx]

        # Print the closest point for each cluster to the data point and determine which cluster is the closest.
        # For every unknown point, the closest red and blue points will be displayed and the cluster which the
        # point falls into will be determined and displayed.
        print()
        print(f'Unknown Point. Index: {u_idx}, Point Coordinates: {u_pt}')
        print(f'Closest Red Point. Index: {min_red_idx}. Distance: {min_red_dist}')
        print(f'Closest Blue Point. Index: {min_blue_idx}. Distance: {min_blue_dist}')
        if min_blue_dist == min_red_dist: # They should never be equal. Only if the same file is loaded for both red and blue.
            cluster = "black"  # This should never be the case but will be noted if it is.
            closest_pt = min_blue_pt
        elif min_blue_dist < min_red_dist:
            cluster = "blue"
            closest_pt = min_blue_pt
        else:
            cluster = "red"
            closest_pt = min_red_pt
        print(f'Unknown Point Index: {u_idx}, {u_pt} falls in class: {cluster}')

        # The lines_list list will be appended with current unknown point, the closest point and its cluster.
        # This list will be used by the create_NNC_plot function.
        closest_info = (u_pt, closest_pt, cluster)
        lines_list.append(closest_info)

        # Append the output file to be saved as a text file.
        known_points.append((u_pt, cluster))
        output_text_2 += f'{u_pt} {cluster}\n'
        for pt in u_pt:
            output_text3 += f'{pt} '
        output_text3 += f'{cluster}\n'

        # This output file option will have the same format as the last line of the print statements shown on the CLI.
        output_text += f'Unknown Point Index: {u_idx}, {u_pt} falls in class: {cluster.title()}\n'

    # remove the carriage return in the last line of the file.
    output_text = output_text.rstrip()
    output_text_2 = output_text_2.rstrip()

    ############ Format the lists for Plotting ################
    # Set the initial width and radius of the points to be plotted.
    width_1 = 1.5
    width_known = 1.5
    radius_1 = 3
    radius_known = 4

    # The function reformat_list in the iodata module will take in the list and other parameters about the points.
    # The lists of data points will be reformatted with the appropriate colours before being plotted in the create_NNC_plot function.
    red_points = reformat_list(red_data, 'red', 'red', width_1, radius_1)
    blue_points = reformat_list(blue_data, 'blue', 'blue', width_1, radius_1)

    # The format for the known points list is different from the other lists as the colour information is already contained.
    #  This requires a different function to reformat the list for the create_NNC_plot function.
    known_points_2 = reformat_known_list(known_points, 'white', width_known, radius_known)
    # Display the output text on the CLI
    print()
    print(output_text)
    # A tuple is returned to the main program that called this function. It contains:
    # All the points that need to be plotted for the three datasets.
    # A list of known points to their nearest neighbour in the existing clusters.
    # Output texts that will be used for display purposes and to save the output file.
    return([red_points, blue_points, known_points_2], lines_list, output_text, output_text_2,)

###################################### K-Means Classifier Function #####################################################
# This will classify the each datapoint in the loaded dataset into a certain cluster of a predetermined amount.
# The algorithm will first pick n random cluster centres and then calculate which cluster is closest to each point.
# That point will then be tagged to that cluster. The cluster's centre point will then be recalculated by centering itself
# in the mean coordinates of all the cluster points. This process will reiterate until the cluster centre does not change
# significantly. The calculated cluster centres, a list of the datapoints belonging to each cluster and output text to
# be saved will be returned to the prgram that called it.

def K_means_classifier(dataset, clust_num, conv_tol, num_iter):
    #################### THIS WILL OPTIMIZE THE CENTROIDS OF THE CLUSTERS USING K-MEANS CLUSTERING ############

    dimensions = len(dataset[0])
    # The function random_cluster_centres is called.
    # Set an initial random starting point for every cluster
    # K_cent is a list of random starting points for the number of defined clusters. the random_cluster_centres function
    # is called to have initial cluster centres randomly distributed among the data points.
    K_cent = random_cluster_centres(clust_num, dimensions)

    # Zero Division Error set to false.
    # A zero_division_error occurs when 1 or more of the randomly selected initial centre points for a cluster are
    # not the closest to any of the points in the randomly selected datapoints. If this is the case, all centroids will be
    # randomly selected again and again until all of them have at least one data point in their cluster.
    # The algorithm will then recalculate all the centroids until convergence is reached.
    zero_div_error = False
    zde_calls = 0

    # Convergence set to false
    conv = False
    # The number of times convergence is reached within the number of iterations entered by the user will be counted.
    conv_cnt = 0

    # Various lists and tuples have been assigned in this algorithm to store information on the cluster centres and
    # their current_clust_cent. contains the iteration number and the cluster centres for that iteration. It will be
    # appended to clust_cent_histry which records the cluster centres for every iteration.
    current_clust_cent = (0, tuple(K_cent))
    clust_cent_hist = []
    clust_cent_hist.append(tuple(current_clust_cent))

    # clust_dist_hist = [] contains a list of the cluster distances of all clusters for every iteration. This will
    # be used to determine when covnvergance is reached (change in difference the specified convergence tolerance
    # and also to find the best combination of cluster centres (where to sum of all distances to their cluster centre
    # is a minimum).
    clust_dist_hist = []
    # clust_lists_hist will store a list of datapoints for every cluster over every iteration. It will be referenced
    # to get the best cluster combinations later.
    clust_lists_hist = []
    # maybe delete the one below
    # all_points_and_cluster = []

    # Iteration will start at 1, not 0
    itr = 1
    # This loop will continue until the specified number of iterations has been reached.
    while itr <= num_iter:

        print()
        print(f'Iteration: {itr}')
        # If there was a division by zero meaning at least one cluster did not have any points closest to it
        # The cluster centres will be randomly redistributed.
        if (zero_div_error == True):
            K_cent = random_cluster_centres(clust_num, dimensions)
            print(f'Zero div error activated in itr: {itr-1}')
            print(f'New cluster centres are: {K_cent}')
            zero_div_error = False

        # If convergence has been reached, the convergence counter is incremented and new random points will be selected.
        # This is done in case a "local minmimum" of cluster distances was found in the previous convergence.
        # It is possible that a better combination of clusters will be found in the following convergences.
        # After the desired number of iterations has been reached, the cluster centres with the best convergence score
        # (smallest distances) will be selected as the final cluster centres combination.
        if conv == True:
            K_cent = random_cluster_centres(clust_num, dimensions)
            print(f'Convergence achieved in itr: {itr-1}')
            print(f'New cluster centres are: {K_cent}')
            conv = False

        # For every iteration, create 2 new lists that both contain a list for each cluster with the following variables:
        # k_list is: [cluster_number, number of points in cluster, sum of x coords, sum of y coords, ..., sum of n coords]
        # k_list will be appended to cluster_info
        # cluster_info: [[k_list0], [k_list[1], ...[k_list[N]]
        # K_centre A list containing the centroid coordinates for each dimension.
        # K_centre: [centre_x, centre_y ..., centre_n] This will be initially empty and calculated after the loop.
        # cluster_centres is a list of lists, 1 for each dimension. the lists are K_centre
        cluster_info = []
        cluster_centres = []
        for i in range(len(K_cent)):
            k_list = [0, 0]
            K_centre = []
            for j in range(dimensions):
                k_list.append(0)
                K_centre.append(0)
            k_list[0] = i
            cluster_info.append(k_list)
            cluster_centres.append(K_centre)

        # This function will loop through all the points in the dataset and calculate which current centre is the closest.
        # The outer loop iterates through all the data points in the dataset
        # The Sum of Squares Error counter is set to 0 initially. This will calculate the square of all the distances
        # of each point to their closest cluster centre. The lower this sum, the better the cluster centres fit to the data.
        sse = 0

        # cluster_lists is of clusters containing the number of points in that cluster and a list of all the points.
        cluster_lists = []
        for i in range(clust_num):
            cluster_lists.append([0, []])

        # For all the points in the dataset
        for idx in range(len(dataset)):
            # The first cluster is initially set as the closest
            closest_centre_idx = K_cent[0]
            # Its distance is calculated
            shortest_distance = calc_distance(dataset[idx], K_cent[0])
            # For every cluster, the distance to the current data point is calculated.
            for ctr_idx in range(len(K_cent)):
                dist_to_ctr = calc_distance(dataset[idx], K_cent[ctr_idx])
                # If the distance from the cluster centre to the data point is shorter,
                # The cluster will be associated with the data point.
                if dist_to_ctr <= shortest_distance:
                    # shortest distance
                    shortest_distance = dist_to_ctr
                    # cluster index of the shortest distance
                    closest_centre_idx = ctr_idx

            # After the loop for the current data point through all the cluster centres terminates:
            # The SSE or its distance to its cluster centre is added to the SSE for all points.
            # The cumulative total is the SSE of how well the data points fit to the cluster centres.
            # The lower the value of SSE the better the cluster centroids fit.
            sse += shortest_distance**2

            # The data point is added to its cluster list and the number of points in that cluster is incremented.
            cluster_lists[closest_centre_idx][1].append(tuple(dataset[idx]))
            cluster_lists[closest_centre_idx][0] += 1

            # For the closest cluster to the current data point:
            # 1. Increment the count of points
            cluster_info[closest_centre_idx][1] += 1
            # 2. Update the sum of all coordinate dimensions to the total for that dimension.
            # This will be used to determine convergence.
            for i in range(dimensions):
                cluster_info[closest_centre_idx][i + 2] += dataset[idx][i]

        # After every datapoint has been run:
        # The pertinent information will be stored.
        clust_lists_hist_entry = (itr, tuple(cluster_lists))
        clust_lists_hist.append(tuple(clust_lists_hist_entry))

        # After having gone through all the data points:
        # Calculate the centre of each coordinate per cluster. The function calculate_centroid is called.
        # It returns updated cluster centres and other associated information.
        centre_function = calculate_centroid(cluster_info, cluster_centres, dimensions, K_cent, zde_calls, zero_div_error)
        cluster_info = centre_function[0]
        cluster_centres = centre_function[1]
        dimensions = centre_function[2]
        zde_calls = centre_function[4]
        zero_div_error = centre_function[5]

        # Convert all the lists of coordinates in cluster_centres to tuples.
        t_cc = []
        for i in cluster_centres:
            j = tuple(i)
            t_cc.append(j)
        t_cc = tuple(t_cc)
        # The current cluster centres are stored along with their iteration number for future reference.
        current_clust_cent = (itr, tuple(t_cc))
        clust_cent_hist.append(tuple(current_clust_cent))
        # Plot some information from the current iteration.
        print(f'For itr {itr - 1}: Previous cluster centres: {clust_cent_hist[-2][1]}')
        print(f'For itr {itr}: Current cluster centres after re-centring: {clust_cent_hist[-1][1]}')
        # Update K_cent to new cluster centres
        K_cent = cluster_centres

        # Calculate the distance between current and previous cluster centres for every cluster and append them to
        # the temporary list change_clust_dist[].
        change_clust_dist = []
        for idx in range(clust_num):
            change_clust_dist.append(calc_distance(clust_cent_hist[-1][1][idx], clust_cent_hist[-2][1][idx]))
        # Calculate the sum for all cluster distances
        change_clust_dist_tot = sum(change_clust_dist)
        print(f'Convergance or Total Distance change between current and previous cluster centres: {change_clust_dist_tot}')
        print(f'Total SSE of all points to their cluster centre: {sse}')

        # Append the total cluster distance differences and the Sum of Squares Error (SSE) of all points to their
        # cluster centres to the cluster distance history list.
        clust_dist_hist.append(tuple((itr, change_clust_dist_tot, tuple(change_clust_dist), sse)))

        if itr > 1:
            print(f'Individual cluster distance change from previous iteration: {clust_dist_hist[-1][2]}')
            print(f'Change in SSE of all points from previous: {sse - clust_dist_hist[-2][3]}')
            print(f'SSE of all points from previous centre: {clust_dist_hist[-2][3]}')

        # If the total change in distance between the current cluster centres and the previous cluster centres is below
        # the entered threshold then convergence has been reached.
        if change_clust_dist_tot < conv_tol:
            print(f"Convergance Threshold of less than {conv_tol} has been reached!")
            print("New random start positions will be set.")
            conv_cnt += 1
            conv = True
        # End of the iteration, the iteration counter will be incremeneted.
        itr += 1

    ################# End of Iterations Loop ###################################################
    # After all the iterations have been completed. Display some summary stats.
    print()
    print("Summary of iterations.")
    print(f'Number of dimensions: {dimensions}')
    print(f'Number of clusters: {len(clust_cent_hist[-1][1])}')
    print(f'Number of Iterations: {itr - 1}')
    print(f'Covergance threshold: {conv_tol}')
    print(f"Number of random start point resets: {zde_calls}")
    print(f'Number of convergences: {conv_cnt}')

    # Find the minimum square of the total of cluster distances of all points to their centre (SSE) by looking at
    # the stored distance history. This is where the cluster centres are in their optimum locations.
    best_sse = clust_dist_hist[0][3]
    best_itr = clust_dist_hist[0][0]
    for i in range(len(clust_dist_hist)):
        if clust_dist_hist[i][3] < best_sse:
            best_sse = clust_dist_hist[i][3]
            best_itr = clust_dist_hist[i][0]
            min_idx = i

    # As was requested, best_centroids is a list of tuples, where each tuple contains the coordinates of all
    # dimensions for each centroid or cluster centre point.
    best_centroids = list(clust_cent_hist[best_itr][1])
    print(f'Best Iteration: {best_itr}. Minimum Sum of Squares Error: {best_sse}')
    print(f'The best combination of cluster centroids is {best_centroids}')

    # The colours in the output file will match those of the plot.
    K_col = ('red', 'green', 'black', 'orange', 'violet', 'blue', 'brown',
             'pink', 'yellow', 'purple', 'silver', 'grey', 'navy', 'aqua', 'teal', 'magenta')

    # Iterations count starts at 1, list count at 0 so cluster of best fit at index [min_itr-1]
    cluster_of_best_fit = clust_lists_hist[best_itr-1][1]

    # As was requested in the assignment, the final cluster allocations of the data points is a list of tuples.
    # list_of_best_fit is a list containing tuples.
    # Each tuple is a tuple of datapoints belonging to each cluster (corresponding to the index of the tuple).
    # Each of those tuples contain the coordinates of each data point of all dimensions.
    list_of_best_fit = []
    for i in range(len(cluster_of_best_fit)):
        list_of_best_fit.append(tuple(cluster_of_best_fit[i][1]))
    print(f'Final cluster list of best fit: {list_of_best_fit}')
    
    print()
    print('Cluster Numbers')
    for i in range(len(cluster_of_best_fit)):
        if i > 15:
            colour = 'black'
        else:
            colour = K_col[i]
        print(f'Cluster: {i+1}, Colour: {colour}, Number of Points: {cluster_of_best_fit[i][0]}')

    # Prepare the output text that will be saved as a text file.
    # It will have header for each cluster that shows the cluster number, the number of points that belong to that
    # cluster and the coordinates of the cluster centre. the next rows will contain a tuple of each point within
    # that cluster.
    output_text = ""
    # Create final text output
    for i in range(len(best_centroids)):
        if i > 15:
            colour = 'black'
        else:
            colour = K_col[i]
        output_text += f'Cluster {i+1}, {colour.title()}. Number of points in cluster: {len(list_of_best_fit[i])}, ' \
        f'Cluster Center Coordinates: {best_centroids[i]}\n'
        for j in range(len(list_of_best_fit[i])):
            output_text += f'{list_of_best_fit[i][j]}\n'
        output_text += '\n'
    output_text = output_text.rstrip()

    print()
    print(output_text)

    # The relevant information to plot the clusters and store the output file are returned to the main program.
    return (list_of_best_fit, best_centroids, zde_calls, conv_cnt, best_itr, best_sse, output_text)

########################################################################################################################
########################################### Def Create Plot ############################################################
# This function is called by the main program after it the Nearest Neighbor Classifer algorithm has been successfully run
# and the required lists have been returned. It will plot the red and blue clusters along with the unknown points
# marked in the colour of their designated cluster. The plot will be plotted on the canvas in the GUI.

def create_NNC_plot(canvas, ip_array,lines_array):

    # Variables to adjust the scaling and placement of the plots are defined and set.
    MIN_X = -2.1
    MAX_X = 8
    MIN_Y = -2.1
    MAX_Y = 8

    s = 60  # scale factor will spread the plots to fit better on the canvas.
    # Horizontal and vertical offsets.
    ext_x = 250
    ext_y = 163

    # Dimensions of x and y coordinates
    xi = 0
    yi = 1
    # Initial comments and coordinate frame are displayed.
    canvas.create_text(425, 10, text="This plot is only completely accurate for 2 dimensional data points", font=('Arial 11 bold'))
    canvas.create_text(425, 25, text = "Unknown points plotted as the same colour of their determined cluster but with a white " \
                                        "outline and a line to the closest point.",font = ('Arial 11'))
    canvas.create_line(MIN_X * s + ext_x, MIN_Y * s + ext_y, MIN_X * s + ext_x, MAX_Y * s + ext_y, fill="black")
    canvas.create_line(MIN_X * s + ext_x, MAX_Y * s + ext_y, MAX_X * s + ext_x, MAX_Y * s + ext_y, fill="black")
    canvas.create_line(MAX_X * s + ext_x, MAX_Y * s + ext_y, MAX_X * s + ext_x, MIN_Y * s + ext_y, fill="black")
    canvas.create_line(MIN_X * s + ext_x, MIN_Y * s + ext_y, MAX_X * s + ext_x, MIN_Y * s + ext_y, fill="black")

    # Plot the three groups of data points.
    for list in ip_array:
        for pts in list:
            x = pts[0][xi] * s + ext_x  # Some values are negative and have been scaled. This offest will centre the points.
            y = pts[0][yi] * s + ext_y # Some values are negative and have been scaled. This offest will centre the points.
            canvas.create_oval(x - pts[4], y - pts[4], x + pts[4], y + pts[4],
            fill=pts[1], outline=pts[2], width = pts[3])

    # Plot the lines between the unknown points and their closest point.
    # Only the x and y coordinates are plotted. For higher dimensional points, xi and yi can be changed up to the number of dimensions.
    # For the given datasets, the points for the 2D and the 4D data sets were very close together, so it is hard to see
    # most lines in the plot. For 8D, as only 2 coordinates can be plotted, the distances to the closest points
    # can seem a bit illogical but they are correct.
    # As the range of all data points in all the files is roughly between -2 and 8, the dimensions of the canvas display
    # are designed to cover any point within this range and so some plots ay appear to be rather zoomed out.
    for ln in range(len(lines_array)):
        canvas.create_line(lines_array[ln][0][xi] * s + ext_x, lines_array[ln][0][yi] * s + ext_y,
                      lines_array[ln][1][xi] * s + ext_x, lines_array[ln][1][yi] * s + ext_y, fill = lines_array[ln][2])
        
########################################################################################################################
##################################### Create K Means Plot ##############################################################
# This function is called by the main program after it the K-Means Classifer algorithm has been successfully run
# and the required lists have been returned. It will plot the cluster centres in unique colours and connect all the
# points belonging to its cluster with a line.

def create_K_Means_plot(canvas, list_of_best_fit, best_centroids, clust_num):
    # This function will plot the required output of the cluster allocations in the GUI.

    MIN_X = -2.1
    MAX_X = 8
    MIN_Y = -2.1
    MAX_Y = 8

    # Define a list of cluster colours.
    K_col = ('red', 'green', 'black', 'orange', 'violet', 'blue', 'brown',
             'pink', 'yellow', 'purple', 'silver', 'grey', 'navy', 'aqua', 'teal', 'magenta')

    s = 58  # scale factor will spread the plots to fit better on the canvas.
    r = 3.5  # radius will be used to increase the size of the points.
    # Horizontal and vertical offsets.
    ext_x = 220
    ext_y = 147

    # Inital comments and coordinate frame are displayed.
    canvas.create_text(375, 12, text="This plot is only completely accurate for 2 dimensional data points:",
                  font=('Arial 12 bold'))
    canvas.create_line(MIN_X * s + ext_x, MIN_Y * s + ext_y, MIN_X * s + ext_x, MAX_Y * s + ext_y, fill="black")
    canvas.create_line(MIN_X * s + ext_x, MAX_Y * s + ext_y, MAX_X * s + ext_x, MAX_Y * s + ext_y, fill="black")
    canvas.create_line(MAX_X * s + ext_x, MAX_Y * s + ext_y, MAX_X * s + ext_x, MIN_Y * s + ext_y, fill="black")
    canvas.create_line(MIN_X * s + ext_x, MIN_Y * s + ext_y, MAX_X * s + ext_x, MIN_Y * s + ext_y, fill="black")

    # Dimensions of x and y coordinates
    xi = 0
    yi = 1

    # Plot the data points.
    # The outer loop goes through the data points sorted by groups of their final cluster allocation
    for idx in range(len(list_of_best_fit)):
        # Range of colours is for up to 15 clusters. If there are more than 15 they will be shown as black.
        for pts in range(len(list_of_best_fit[idx])):
            if idx > 15:
                col1 = 'white'
                col2 = 'black'
            else:
                col1 = K_col[idx]
                col2 = K_col[idx]

            # Only two dimensions can be shown. xi and yi are set to 0 and 1 so the first two dimensions of each cluster
            # will be plotted.
            x1 = list_of_best_fit[idx][pts][xi] * s + ext_x  # some values are negative so +ext is to make them positive so they fit on the canvas.
            y1 = list_of_best_fit[idx][pts][yi] * s + ext_y
            canvas.create_oval(x1 - r, y1 - r, x1 + r, y1 + r, outline=col1, fill=col2)
            # Lines are plotted from each point to their cluster centroid.
            x2 = best_centroids[idx][xi] * s + ext_x
            y2 = best_centroids[idx][yi] * s + ext_y
            canvas.create_line(x2, y2, x1, y1, fill=col1)

    # Plot best centroids
    r2 = 4.5
    for k in range(clust_num):
        if k > 15:
            col1 = 'white'
            col2 = 'black'
        else:
            col1 = 'white'
            col2 = K_col[k]

        x = best_centroids[k][xi] * s + ext_x
        y = best_centroids[k][yi] * s + ext_y
        canvas.create_oval(x - r2, y - r2, x + r2, y + r2, outline=col1, fill=col2, width=2)

########################################################################################################################