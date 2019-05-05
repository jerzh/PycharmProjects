bound = 100
primes = []
for n in xrange(2, bound):
    prime = True
    for p in primes:
        if n % p == 0:
            prime = False
            break
        if p * p > n:
            break
    if prime:
        primes.append(n)
print(primes)
