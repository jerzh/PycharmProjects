# converted to c++ (python too slow)

from __future__ import division
import random

total = 0
num_iter = 100000


def move(p, x):
    p += x
    if p < 0 or p >= 5:
        p %= 5
    return p


for j in xrange(num_iter):
    pos = 0
    count = 0
    for i in xrange(2019):
        if random.randint(0, 1) == 0:
            pos = move(pos, -1)
        else:
            pos = move(pos, 1)
        if pos == 0:
            count += 1
    total += count

    if j % 100 == 0:
        print str(j) + ': ' + str(total / (j + 1))
