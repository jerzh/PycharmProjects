"""
ID: jeremy.11
LANG: PYTHON2
TASK: skidesign
"""
fi = open("skidesign.in")
with open("skidesign.out", "w") as fo:
    n = int(fi.readline())

    # read the heights and determine the smallest and largest
    small = 100
    large = 0
    hills = []
    for i in xrange(n):
        height = int(fi.readline())
        if height < small:
            small = height
        if height > large:
            large = height
        hills.append(height)

    # iterate through every possible range
    diff = large - small - 17
    large = small + 17
    if diff > 0:
        min_cost = 10000000
        for i in xrange(diff + 1):
            cost = 0
            for h in hills:
                if h < small:
                    cost += (small - h)**2
                elif h > large:
                    cost += (h - large)**2
            if cost < min_cost:
                min_cost = cost
            small += 1
            large += 1
        fo.write(str(min_cost) + "\n")
    else:
        fo.write(str(0) + "\n")
