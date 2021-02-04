def main():
    print(sum(10))

def sum(x):
    #Assuming x >= 1
    #Complete this function recursively
    if x ==1:
        return 1
    else:
        return x + sum(x-1)

main()