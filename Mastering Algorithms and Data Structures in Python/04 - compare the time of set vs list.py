# Define a function to demonstrate the operation and time complexity of a hash set
def hash_set_operations():
  
    # Importing the necessary libraries
    import time
    
    # Create a hash set and a list
    hash_set = set()
    list_data = []
    
    # Setting the range for the data elements
    data_range = 10**7
    
    # Adding elements to the hash set and the list
    for i in range(data_range):
        hash_set.add(i)
        list_data.append(i)
        
    # Define a test element (which is out of the data range and thus is not present in both the list and set)
    test_element = data_range + 1
    
    # Start the clock and check for the presence of the test elements in the set
    start_time = time.time()
    print("Hash Set Test Result:", test_element in hash_set)
    print("Searching in the Hash Set Took:", time.time() - start_time)
  
    # Start the clock and check for the presence of the test elements in the list
    start_time = time.time()
    print("List Test Result:", test_element in list_data)
    print("Searching in the List Took:", time.time() - start_time)

# Call the function
hash_set_operations()
