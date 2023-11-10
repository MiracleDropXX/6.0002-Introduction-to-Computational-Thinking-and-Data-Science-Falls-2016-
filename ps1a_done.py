###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    file = open(filename, 'r')
    cow_data = file.readlines()
    
    cow_dict = {}
    
    for line in cow_data:
        tmp = line.strip().split(',')
    
        cow_dict[tmp[0]] = int(tmp[1])
        
    return cow_dict
    pass

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # cow sorted by weight
    cows_sorted = {cow_name: cow_weight for cow_name, cow_weight in sorted(cows.items(), key = lambda item:item[1], reverse = True)}
    trip_overview =[]
    # initialize output 
    if limit < min(cows_sorted.values()):
        print ('Are you Nuts, your smallest cow is: ' + str(min(cows_sorted.values())))
        return trip_overview, len(trip_overview) 
    else:
        eligible_cow = {cow_name: cow_weight for cow_name, cow_weight in cows_sorted.items() if not(isinstance(cow_weight, int) and (cow_weight > limit))}
        while len(eligible_cow) != 0:
            budget_trip = limit
            current_trip = [] # list of cow
            while budget_trip >0:
                for cow_candidate in eligible_cow.copy().keys():
                    if eligible_cow[cow_candidate] <= budget_trip:
                        current_trip.append(cow_candidate)
                        budget_trip += -eligible_cow[cow_candidate]
                        
                        eligible_cow.pop(cow_candidate)
                if len(eligible_cow)== 0:
                    trip_overview.append(current_trip)
                    return trip_overview, len(trip_overview) 
                elif budget_trip < min(eligible_cow.values()):
                        budget_trip = 0
                        #add trip to trip result
                        trip_overview.append(current_trip)

    pass


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    num_trip = []
    
    for cow_partition in get_partitions(cows):
        # compute weight per trip of all trip
        # if any exceed, give numptrip with inf
        total_load_tmp_trip= []
        for tmp_trip in range(len(cow_partition)):
            total_load_tmp_trip.append(sum([cows.get(cow_in_trip) for cow_in_trip in cow_partition[tmp_trip]]))
      
        if max(total_load_tmp_trip) > limit:
            num_trip.append(float('inf'))
        else: 
            num_trip.append(len(cow_partition))
    trip_list = list(get_partitions(cows))
    trip_detail = trip_list[num_trip.index(min(num_trip))]
    
    return(trip_detail, min(num_trip))
    pass
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start_greedy = time.time()
    greedy_cow_transport(cows = ps1_cow_dict, limit = 10)
    end_greedy = time.time()
    print('run time of greedy is: ' + str(end_greedy - start_greedy))
    
    
    start_bf = time.time()
    brute_force_cow_transport(cows = ps1_cow_dict, limit = 10)
    end_bf = time.time()
    print('run time of brute force is: ' + str(end_bf - start_bf))
    
    pass 


### testing 
if __name__ == '__main__':
    print("I load all cows from farm 1 \n")
    ps1_cow_dict = load_cows('ps1_cow_data.txt')
    print("I transport them with greedy algorithm \n")
    ps1_trip_greedy, n_trip_greedy = greedy_cow_transport(cows = ps1_cow_dict, limit = 10)
   
    print(f'Greedy transport detail: {ps1_trip_greedy} in minimum number of trip: {n_trip_greedy} \n')
    
    print("I transport them with brute force algorithm \n")
    ps1_trip_bruteforce, n_trip_brute_force = brute_force_cow_transport(cows = ps1_cow_dict, limit = 10)
    print(f'Brute force transport detail: {ps1_trip_bruteforce} in minimum number of trip: {n_trip_brute_force}')

    compare_cow_transport_algorithms()
    time 

# Problem A.5: Writeup
# Answer the following questions in a PDF file called ps1_answers.pdf.
# 1. What were your results from compare_cow_transport_algorithms? Which 
# algorithm runs faster? Why?
# Greedy is the faster algorithm since once it found the solution deemed optimal, the algorithm stops, which is why some time the solution s not optimal.  Brute force as the name indicates, look at all possible combination, in this case the power set of 2 to the numer of cows...
# 2. Does the greedy algorithm return the optimal solution? Why/why not?
# no, because by definition, it looks for the most next "optimum" element which can be not optimal (for example adding two other following elements whose sum is higher than the pre-assumed optimal element)
# 3. Does the brute force algorithm return the optimal solution? Why/why not?
# Yes. because it look at all possible cases
