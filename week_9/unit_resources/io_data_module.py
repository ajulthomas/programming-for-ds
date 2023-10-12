
##########################
#Nearest Neighbour Classifier
##########################

#Function to run Nearest Neighbour Classifier
def run_nearest_neighbour(blue_filename, red_filename, unknown_filename):
    #Read data
    blue_list = read_multi_dim_data_file(blue_filename)
    red_list = read_multi_dim_data_file(red_filename)
    unknown_list = read_multi_dim_data_file(unknown_filename)
    #print(*blue_list, sep='\n')
    #print(red_list)
    #print(unknown_list)

    output = ''
    for unknown in unknown_list:
        dist = 0
        min_dist_red = 2147483648
        nearest_red = ()
        for sample in red_list:
            dist = calculate_distance(unknown, sample)
            if dist < min_dist_red:
                min_dist_red = dist
                nearest_red = sample

        dist = 0
        min_dist_blue = 2147483648
        nearest_blue = ()
        for sample in blue_list:
            dist = calculate_distance(unknown, sample)
            if dist < min_dist_blue:
                min_dist_blue = dist
                nearest_blue = sample

        classified = ''
        if min_dist_blue < min_dist_red:
            classified = 'blue'
            nearest = nearest_blue
        else:
            classified = 'red'
            nearest = nearest_red

        # Output to screen
        for u in unknown: 
            output += str(u) + ' '
        output += classified + '\n'
    return output
#end of function

##########################
#K-means clustering
##########################

#Function to run K-means Clustering
def run_kmeans (K=2, data_filename=None):
    if data_filename == None:
        print('No input filename')
        return
    #1. Read data file, get number of dimensions D and number of data samples N
    data_list = read_multi_dim_data_file(data_filename)
    N = len(data_list)
    #print('Number of samples N =', N)
    D = len(data_list[0])
    #print('Number of dimensions D =', D)

    #2a. Input number of clusters K, create K clusters having same dimension D at random
    centre_list = [data_list[i] for i in range(K)]
    #print(*centre_list)

    #2b. Set threshold to a small value 
    threshold = 0.1

    round = 1
    while True:
        #3. For each data sample, find its nearest clucter centre
        #4. Group data samples nearest to same cluster centre to form K clusters
        samples_in_cluster_list = find_samples_in_cluster_centres(data_list, centre_list)
        #print(*samples_in_cluster_list, sep='\n')

        #5. For each cluster, calculate new cluster centre
        new_centre_list = calculate_new_cluster_centre_list(samples_in_cluster_list)
        #print(*new_centre_list)

        #6. For each cluster, calculate distance between old and new cluster centres. Calculate sum of all these distances
        sum = 0
        for i in range(K):
            sum += calculate_distance(centre_list[i], new_centre_list[i])

        #7. If the sum is less than the threshold: 
        #      output K cluster centres then break 
        #   else: 
        #      set cluster centres to new cluster centres
        #print(f'{runs}. sum = {sum}')
        if sum < threshold:
            break
        else:
            centre_list = new_centre_list.copy()
            round += 1
    #print('The algorithm converged after ', round, ' rounds.')
    return centre_list
#end of function

##########################
#Functions
##########################

#Function to find nearest cluster centre for each data sample
def find_samples_in_cluster_centres(data_list, centre_list):
    number_of_clusters = len(centre_list)
    samples_in_clusters = []
    for k in range(number_of_clusters):
        samples_in_clusters.append([])
    #print(samples_in_clusters)
    for i in range(len(data_list)):
        shortest_distance = 2147483648
        nearest_centre_index = 0
        for k in range(number_of_clusters):
            dist = calculate_distance(data_list[i], centre_list[k])
            if shortest_distance > dist:
                shortest_distance = dist
                nearest_centre_index = k
        samples_in_clusters[nearest_centre_index].append(data_list[i])

    for i in range(len(samples_in_clusters)):
        if len(samples_in_clusters[i]) == 0: #cluster empty
            #print(samples_in_clusters[i])
            samples_in_clusters[i].append(data_list[0])

    return samples_in_clusters
#end function

#Function to calculate new cluster centre
def calculate_new_cluster_centre_list(samples_in_clusters):
    number_of_clusters = len(samples_in_clusters)
    new_centre_list = []
    for k in range(number_of_clusters):
        data_samples = samples_in_clusters[k]
        number_of_dimensions = len(data_samples[0])
        new_centre = [0 for i in range(number_of_dimensions)]
        N = len(data_samples)
        for d in range(number_of_dimensions):
            sum = 0
            for sample in data_samples:
                sum += sample[d]
            new_centre[d] = sum / N
        new_centre_list.append(new_centre)
    return new_centre_list
#end function

#Function to read multi-dimensional data from file and 
#return data as a list of tuples
def read_multi_dim_data_file(filename):
    dataset = [] #dataset is a python list 
    f = None
    try:
        f = open(filename, 'r')
        while True:
            line = f.readline()
            if len(line) > 1: #line not empty
                line = line.replace('\n', '') #remove end of line \n character
                string_list = line.split(' ') #x y z ... coordinates in string format
                sublist = [float(x) for x in string_list]
                dataset.append(tuple(sublist))
            else:
                break;
    except Exception as ex:
        print(ex.args)
    finally:
        if f:
            f.close()
    return dataset
#end of function

#define function 
def calculate_distance(p1, p2):
    d = 0
    for i in range(len(p1)):
        d += (p2[i] - p1[i]) * (p2[i] - p1[i]) 
    d = d**0.5
    return d
#end function

#define function
def find_nearest_centre(data_sample, centre_list):
    shortest_distance = 2147483648
    nearest_centre = []
    for centre in centre_list:
        dist = calculate_distance(data_sample, centre)
        if shortest_distance > dist:
            shortest_distance = dist
            nearest_centre = centre
    return nearest_centre
#end function

#Function to generate K cluster centres at random
def generate_K_cluster_centres(K, D):
    cluster_centre_list = []
    for k in range(K):
        cluster_centre = []
        for d in range(D):
            cluster_centre.append((k+1)/(k+d+1))
        cluster_centre_list.append(cluster_centre)
    return cluster_centre_list
#end of function

