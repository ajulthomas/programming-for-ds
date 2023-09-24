
#Assignment
# module to handle clustering
# method available generate_K_cluster_centers, calculate_all_distances, find_shortest_distance, calculate_memberships, calculate_sum_2, calculate_cluster_centres

## function to initiate k means clustering of data
# takes no. of dimensions, no. of clusters and datasample as input
def k_means_cluster(cluster_size, read_data):
    
    # size of the sample data list
    # sample_size =  len(read_data)

    # no. of dimensions of the data
    num_of_dimension =  len(read_data[0])
    
    cluster_centers = generate_K_cluster_centres(num_of_dimension, cluster_size)
    
    # threshold to a small value
    threshold = 0  ##change the value of 0
    
    # variable to store the list of clustered datasets
    clustered_samples = []

    while True:
        # create a list of cluster lists
        clustered_samples = cluster_samples(cluster_centers, read_data)
        
        # find new cluster centers
        new_cluster_centers = []
        for i in range(len(clustered_samples)):
            new_cluster_centers.append(calculate_cluster_center(clustered_samples[i]))
        
        # print(new_cluster_centers)
        
        # sum of distance between old and new cluster centers
        d = 0
        for c in range(len(cluster_centers)):
            d += calculate_distance(cluster_centers[c], new_cluster_centers[c])
        
        print(f'sum of distance between old and new cluster centers {d}')
        
        if d <= threshold:
            break
        else:
            cluster_centers = new_cluster_centers.copy()
    
    return (cluster_centers, clustered_samples)
## end of function    

## function to calculate distance
def calculate_distance(point1, point2):
    distance = 0
    ##write your code here.
    for i in range(len(point1)):
        distance += (point2[i] - point1[i]) * (point2[i] - point1[i])
        distance = distance**0.5
    return distance
## end of function

## function to find cluster center
def calculate_cluster_center(data_cluster):
    cluster_center = []
    # no. of coordinates of each data point
    dim = len(data_cluster[0])
    
    # total no. of samples
    n = len(data_cluster)
    
    # for each dimension we will calculate the average value
    for d in range(dim):
        sum = 0
        for sample in data_cluster:
            sum += sample[d]
        cluster_center.append(sum/n)
    return tuple(cluster_center)
## end of function

## find the nearest cluster center
def nearest_cluster_center(data_sample, cluster_centers):
    shortest_distance = calculate_distance(data_sample, cluster_centers[0])
    nearest_cc_index = 0
    for i in range(len(cluster_centers)):
        dist = calculate_distance(data_sample, cluster_centers[i])
        if dist < shortest_distance:
            shortest_distance = dist
            nearest_cc_index = i
    return nearest_cc_index
## end of function

## generate random cluster centers
def generate_K_cluster_centres(num_of_coordinate, num_of_clusters):
    r = 3 #int(input("Input a random number:"))
    cluster_centers_list = []
    for k in range(num_of_clusters):
        cluster_center = []
        for d in  range(num_of_coordinate):
            cluster_center.append((k+d+r)/(k+d+1))
        cluster_centers_list.append(tuple(cluster_center))
    return cluster_centers_list
## end of function

## cluster samples based on nearest cluster center
def cluster_samples(cluster_centers, data_samples):
    data_clusters = [ [] for i in range(len(cluster_centers))]
    for sample in data_samples:
        nearest_cluster_center_index = nearest_cluster_center(sample, cluster_centers)
        data_clusters[nearest_cluster_center_index].append(sample)
    return data_clusters
## end of function

