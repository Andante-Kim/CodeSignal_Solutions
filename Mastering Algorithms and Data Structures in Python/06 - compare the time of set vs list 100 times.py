# Create a list and a set
    data_list = []
    data_set = set()

    # Adding elements to list and set
    for i in range(10**6):
        data_list.append(i)
        data_set.add(i)

    # Set and List are ready; now let's define a non-existing item to search for
    test_item = 10**6 + 1  # This item is not in our set or list

    # TODO: Time the 100 consecutive operations of checking whether `test_item` is in `data_set` and print the result and time taken
    start_time = time.time()
    for i in range(100):
        set_result = test_item in data_set
    print("Searching in the Hash set took : ", time.time() - start_time)

    # TODO: Time the 100 consecutive operations of checking whether `test_item` is in `data_list` and print the result and time taken
    start_time = time.time()
    for k in range(100):
        list_result = test_item in data_list   
    print("Searching in the list took : ", time.time() - start_time)

# Execute the function
compare_operations()
