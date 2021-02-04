# Sort a sequence in ascending order using the selection sort  # algorithm
def selectionSort(theSeq,order):
    n = len(theSeq)


    for i in range(n - 1):
        # Assume the ith element is the smallest.
        selected_index = i  # Determine if any other element contains a smaller value.
        for j in range(i + 1, n):
            if order.lower() =='a':
                if theSeq[j] < theSeq[selected_index]:
                    selected_index = j
            elif order.lower()=="d":
                if theSeq[j] > theSeq[selected_index]:
                    selected_index = j


                # Swap the ith value and selected_index value only if the
                # smallest value is not already in its proper position.
        if selected_index != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[selected_index]
            theSeq[selected_index] = tmp


            print(theSeq)#print the result each pass

    # Test codes
list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

print('Input List:', list_of_numbers)
selectionSort(list_of_numbers,'d')
print('Sorted List:', list_of_numbers)
