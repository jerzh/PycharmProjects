"""
ID: jeremy.11
LANG: PYTHON2
TASK: wormhole
"""
import copy

fi = open("wormhole.in")
with open("wormhole.out", "w") as fo:
    n = int(fi.readline())

    # number of wormholes in each row
    rows = {}
    for i in xrange(n):
        line = fi.readline()
        y = int(line.split()[1])
        if y in rows:
            rows[y] += 1
        else:
            rows[y] = 1

    # which wormhole Bessie will reach for each wormhole she exits
    links = {}
    i = 0
    for y in rows:
        for j in xrange(rows[y] - 1):
            links[i] = i + 1
            i += 1
        i += 1

    # cycle through all the possible pairings
    pairs = {}
    remaining = range(n)

    def match(r):  # r for remaining
        if len(r) == 0:
            # determine if loop exists
            for pos in xrange(n):
                loop = True
                for k in range(n):
                    if pos in links:
                        pos = pairs[links[pos]]
                    else:
                        loop = False
                        break
                if loop:
                    return 1
            return 0
        else:
            count = 0
            first = r[0]
            del r[0]
            for second in r:
                pairs[first] = second
                pairs[second] = first
                r2 = copy.deepcopy(r)
                r2.remove(second)
                count += match(r2)
            return count

    fo.write(str(match(remaining)) + "\n")
