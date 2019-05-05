from __future__ import division
import random


def run(n, c):
    coins = [c] * n
    turns = 0
    while True:
        pile = 0
        nonzero = 0
        for i in xrange(len(coins)):  # how many coins are in the pile
            if coins[i] != 0:
                nonzero += 1
                pile += 1
        if nonzero <= 1:  # if the game is over, break
            break
        while True:  # give someone the pile
            player = random.randint(0, n - 1)
            if coins[player] != 0:
                coins[player] += pile
                break
        for i in xrange(len(coins)):  # take away the 1 coin from before
            if coins[i] != 0:
                coins[i] -= 1
        turns += 1  # counter!
    return turns


def avg(n, c, iterations):
    total = 0
    for i in xrange(iterations):
        total += run(n, c)
    return total / iterations


print avg(3, 2, 100000)
