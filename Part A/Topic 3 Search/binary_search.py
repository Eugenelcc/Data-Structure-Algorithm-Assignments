def binarySearch(theValues,target):
    #start with the entire sequence of elements
    low = 0
    high = len(theValues) - 1

    #Repeatedly subdivide the sequence in half
    # until the target is found
    while low <= high:
        # Find the midpoint of the sequence
        mid = (low + high) // 2

        # Does the midpoint contain the target ?
        # If yes, return midpoint(i.e. index of the list)
        if theValues[mid] == target:
            first_occurrence = mid
            cont = True

            while first_occurrence > 0 and cont:
                if theValues[first_occurrence - 1 ] == target:
                    first_occurrence -= 1
                else:
                    cont = False

            return first_occurrence
        # or is the target before the midpoint ?
        elif target < theValues[mid]:
            high = mid - 1
        # Or is the target after the midpoint ?
        else:
        # Or id the target after the midpoint ?
            low = mid + 1

    return -1


#test Code
list = ["apple",'pear','orange','fish','lemon']
sortedListOfNum = [1,2,7,10,10,18,25,30,33,42,56,61,70,73,88]
print(binarySearch(sortedListOfNum,10))
print(binarySearch(sortedListOfNum,73))
print(binarySearch(list,"lemon"))
