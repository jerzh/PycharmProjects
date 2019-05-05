"""
ID: jeremy.11
LANG: PYTHON2
TASK: pprime
"""
import math


def check(num):
    if num < a or num > b or num % 2 == 0 or num % 3 == 0:
        return
    for i in xrange(6, int(math.floor(math.sqrt(num))) + 2, 6):
        if num % (i - 1) == 0 or num % (i + 1) == 0:
            return
    fo.write(str(num) + "\n")


fi = open("pprime.in")
with open("pprime.out", "w") as fo:
    a, b = map(int, fi.readline().split())
    n_a = int(math.floor(math.log(a, 10)))
    n_b = int(math.floor(math.log(b, 10)))
    for n in xrange((n_a + 1) / 2, (n_b + 1) / 2 + 1):
        for half in xrange(10 ** n, 10 ** (n + 1)):
            half_str = str(half)
            check(int(half_str[:-1] + half_str[::-1]))
        for half in xrange(10 ** n, 10 ** (n + 1)):
            half_str = str(half)
            check(int(half_str + half_str[::-1]))
