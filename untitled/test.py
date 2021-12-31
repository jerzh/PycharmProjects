def fact2(n):
    """ n: int > 0 """
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod


print(fact2(1))
