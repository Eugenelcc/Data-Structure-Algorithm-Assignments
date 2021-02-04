def fib(n):
    assert n >=0

    if n == 1 or n== 0:
        return  n
    else:
        return fib(n-1) + fib(n-2)


#Test Code
for i in range(5):
    print(fib(i), end = ' ')