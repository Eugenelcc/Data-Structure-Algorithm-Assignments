#sort a python list in ascending order using the merge sort
#algorithm
def mergeSort( theList ):

    # Check the base case - the list contains a single item
    if len(theList) <= 1:
        return theList
    else:
        # Compute the midpoint
        mid = len(theList) // 2

        # Split the list and perform the recursive step
        leftHalf = mergeSort( theList[ :mid ] )
        rightHalf = mergeSort( theList[ mid: ] )

        # Merge the two sorted sublists
        newList = mergedSortedLists( leftHalf, rightHalf)
        return newList





#Merge two sorted lists to create and return a new sorted list
def mergedSortedLists(listA,listB):

    #Create the new list and initialise the list markers
    newList = list()
    a = 0
    b= 0

    #Merge the two lists together until one is empty

    while a <len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b+=1

    #If listA contains more items , append remaining items to
    #newList

    while a <len(listA):
        newList.append(listA[a])
        a +=1
    #If listB contains more items, append remaining items to
    #newList
    while b <len(listB):
        newList.append(listB[b])
        b+=1

    return newList

# Test code
list_of_numbers = [12, 7, 9, 24, 7, 29, 5, 3, 11, 7]

print('Input List:', list_of_numbers)
mergeSort(list_of_numbers)

merge_list = mergeSort(list_of_numbers)
print('FInall List',merge_list)