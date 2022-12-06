def find_next_min(num_list,start_index):
    #Remove pass and write the logic to find the minimum element in a sub-list and return the index of the identified element in the num_list.
    #start_index indicates the start index of the sub-list
    nu=min(num_list[start_index::])
    return nu

#Pass different values to the function and test your program
num_list=[10, 20, 30, 1]
start_index=0
print("Index of the next minimum element is", find_next_min(num_list,start_index))
#start_index-0,num_list-[10, 20, 30, 1]
