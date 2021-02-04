def sequentialSearch(theValues,target):
    n = len(theValues)

    for i in range(n):
        # If the target is in the ith element , return True
        if theValues[i] == target:
            return True

    return False # If not found, return False


def SortedsequentialSearch(theValues, target):
    n = len(theValues)

    for i in range(n):
        # If the target is in the ith element , return True
        if theValues[i] == target:
            return True
        elif theValues[i] > target:
            return False

    return False  # If not found, return False


#Test codes
listofNum = [10,7,1,3,-4,2,20]
print(sequentialSearch(listofNum,3))
print(sequentialSearch(listofNum,30))


sortedlistofNum = sorted(listofNum)
print(SortedsequentialSearch(sortedlistofNum,10))
print(SortedsequentialSearch(sortedlistofNum,30))

