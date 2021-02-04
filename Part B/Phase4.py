def SumOfArrayTwoKeys(SEQ, SEQ_size, z):
    # sort the array


    """
    SumOfArrayTwoKeys(SEQ, len(SEQ), z)
    :param SEQ:  #SEQ = [2, 3, 5, 7, 8, 10, 15, 16, 23, 28]
    :param SEQ_size:  10
    :param z: 25
    25  = 23+2
    :return: 28 + 2 = 29 :False
            23+2 = 25 : True
            10+15 = 25 : True

        l = SEQ[0] , SEQ[1] .....
        r = SEQ_size
        l + size = Z

        if Z = 25

        X + Y > 25 ~
        5+23=28
        28>25 r - 1
        5+16 = 21
        21 <25 l -1
        7+16 =23
        23<25 l -1
        8+16 = 24
        24<25 l -1
        10+16 =26
        26>25 r -1
        10+15 = 25  <<<

        25:
        10+15 = 25
        23+2 = 25




    """


    quicksort(SEQ) # Sort into ascending orders
    l = 0 #0,1,2,4,5,6,7,8,9
    r = SEQ_size - 1 #9,8,7,6,5,4,3,2,1

    new_list = []
    # traverse the array for the two elements
    while l < r: #0<9 = True
        if (SEQ[l] + SEQ[r] == z):
            print("X= {}\nY= {}".format(SEQ[l],SEQ[r]))
            return True

        elif (SEQ[l] + SEQ[r] < z):
            l += 1
        else:
            r -= 1

    print("""X = Not found \nY = Not Found""")
    return False


#Sort the list to ascending orders
def quicksort(list):
    if not list:
        return []
    return (quicksort([x for x in list[1:] if x < list[0]])
            + [list[0]] +
            quicksort([x for x in list[1:] if x >= list[0]]))


"""
X + Y  = Z 
"""
# TEST CODE #
SEQ = [2, 3, 5, 7, 8, 10, 15, 16, 23, 28]
print('SEQ:',SEQ)
size = len(SEQ)
Z = int(input("enter a positive integer number: ")) #25
print("Z =",Z)

if (SumOfArrayTwoKeys(SEQ, size, Z)):

    print("TRUE (since X + Y = Z)")
else:
    print("Array doesn't have two elements with the given sum")
    print("""False (since there does not exist two integers X and Y in SEQ, where  X + Y = Z)  """)