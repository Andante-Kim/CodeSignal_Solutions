# Importing the necessary module
import time

# Define a function to demonstrate the operation and time complexity of hash sets
def hash_set_operations():
  
    # Create a new hash set 
    names_set = set()

    # Setting the range for the data elements
    data_range = 10**6

    # Constructing a unique names list
    unique_names = ['Name' + str(i) for i in range(data_range)]

    # Adding elements to the set
    for i in range(data_range):
        names_set.add(unique_names[i]) # unique_names[0] -> unique_names[i]

    # Define a test element (which is out of the data range and thus is not present in the set)
    test_name = 'Name' + str(data_range + 1)

    # Define a test element that should exist
    test_name2 = 'Name' + str(data_range - 1)

    # Start the clock and check for the presence of the test elements in the set
    start_time = time.time()
    print("Hash Set Test Result 1:", test_name in names_set)
    print("Hash Set Test Result 2:", test_name2 in names_set)
    print("Searching in the Hash Set Took:", time.time() - start_time)

# Call the function
hash_set_operations()
