"""
ID: jeremy.11
LANG: PYTHON2
TASK: sprime
"""
import math


def check_prime(num):
    if num == 2 or num == 3:
        return True
    elif num == 1 or num % 2 == 0 or num % 3 == 0:
        return False
    for q in xrange(6, int(math.floor(math.sqrt(num))) + 2, 6):
        if num % (q - 1) == 0 or num % (q + 1) == 0:
            return False
    return True


def superprime_search(n0, num):
    if not check_prime(num):
        return
    if n0 == n:
        fo.write(str(num) + "\n")
    else:
        for d in xrange(1, 10, 2):
            superprime_search(n0 + 1, num * 10 + d)


fi = open("sprime.in")
with open("sprime.out", "w") as fo:
    n = int(fi.readline())
    for d0 in xrange(0, 10):
        superprime_search(1, d0)
