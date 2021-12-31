"""
ID: jeremy.11
LANG: PYTHON3
TASK: holstein
"""
import itertools

fi = open('holstein.in')
with open('holstein.out', 'w') as fo:
    v = int(fi.readline())
    vitamins = [int(s) for s in fi.readline().split()]
    g = int(fi.readline())
    scoops = [[]] * g
    for feed in range(g):
        scoops[feed] = [int(s) for s in fi.readline().split()]

    done = False
    for num_scoops in range(g + 1):
        for combo in itertools.combinations(range(g), num_scoops):
            if all([(sum([scoops[s][i] for s in combo]) >= vitamins[i]) for i in range(v)]):
                fo.write(str(num_scoops) + ' ')
                fo.write(' '.join(map(lambda x: str(x + 1), combo)) + '\n')
                done = True
                break
        if done:
            break
