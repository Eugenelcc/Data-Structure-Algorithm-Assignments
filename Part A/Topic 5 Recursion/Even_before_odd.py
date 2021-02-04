def organize_recurse(theValue,low,high): #0 , 9
    if low < high:
        if theValue[high]% 2 == 0 :

            tmp = theValue[low]
            theValue[low] = theValue[high]
            theValue[high] = tmp
            #Data [low] is known to be even
            print(theValue)
            organize_recurse(theValue,low+1 ,high )
        else:
            #data[high] is known to be high
            organize_recurse(theValue , low , high-1)

#Test code

list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
print('original list :' , list_of_numbers)
print(len(list_of_numbers))
organize_recurse(list_of_numbers,0,len(list_of_numbers)-1)
print('rearragne list :', list_of_numbers)