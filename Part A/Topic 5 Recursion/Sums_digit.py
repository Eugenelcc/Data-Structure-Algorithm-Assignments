def sumDitgits(x):
    assert x >=0

    if x == 0:
        return  0
    else:
        return x % 10 + sumDitgits(x//10)

#test code
print(sumDitgits(368))