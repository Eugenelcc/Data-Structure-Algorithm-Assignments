def recBinarySearch(target,thevalue,low,high):
    if low > high:
        return -1
    else:
        #Find the midpoint of sequence
        mid = (low+high) // 2
        #Does the element at the midpoint contain the target ?
        if thevalue[mid] == target:
            return mid #base case #2
        #or does the target follows the midpoint
        elif target < thevalue[mid]:
            return recBinarySearch(target,thevalue,low ,mid-1)

        #or does the target follows the element at the midpoint ?
        else:
            return recBinarySearch(target,thevalue,mid+1,high)







# Test codes
sortedListOfNum = [1, 2, 7, 10, 18, 25, 30, 33, 42, 56, 61, 70, 73, 88]
print(recBinarySearch(10, sortedListOfNum, 0, len(sortedListOfNum) - 1))
print(recBinarySearch(73, sortedListOfNum, 0, len(sortedListOfNum) - 1))
print(recBinarySearch(12, sortedListOfNum, 0, len(sortedListOfNum) - 1))
