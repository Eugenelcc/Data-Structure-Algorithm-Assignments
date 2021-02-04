def isPalidrome(astr):
    #Base case
    if len(astr)<=1:
        return True
    return astr[0] == astr[-1] and \
        isPalidrome(astr[1:len(astr)-1]) #Recursive case

#Test code
while True:
    astr = input("Enter a string (q to quit): ")
    astr = astr.lower()
    if astr =='q':
        break

    #Strip all non alphanumeric characters from aStr
    astr = ''.join(ch for ch in astr if ch.isalnum())

    # Call isPalidrome() to determine if astr is a palidrome
    is_a_palindrome = isPalidrome(astr)

    if is_a_palindrome:
        print("'{}' is a palindrome. ".format(astr))
    else:
        print("'{}' is not a palindrome. ".format(astr))