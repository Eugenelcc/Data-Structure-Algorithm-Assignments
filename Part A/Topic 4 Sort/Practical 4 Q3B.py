def last_element(tuple):
    return tuple[-1]




def sort_by_last_element(tuples_list):
    return sorted(tuples_list, key=last_element)



# Test Codes
tuple_list = [(1,7),(1,3),(3,4,5),(2,2)]
print(sort_by_last_element(tuple_list))