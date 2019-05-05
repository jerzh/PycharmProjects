"""
ID: jeremy.11
LANG: PYTHON2
TASK: milk3
"""
fi = open("milk3.in")
with open("milk3.out", "w") as fo:
    capacities = tuple(int(s) for s in fi.readline().split())  # yuh python
    # print capacities
    states = set()
    pos_c = set()

    def dfs(*args):
        # print args
        if args in states:
            return
        states.add(args)
        if args[0] == 0:
            pos_c.add(args[2])

        for i in xrange(3):
            for j in xrange(3):
                if i == j:
                    continue
                # print str(i) + " " + str(j)
                # pour bucket i into bucket j
                args2 = list(args)
                if args[j] + args[i] > capacities[j]:
                    args2[i] = args[i] + args[j] - capacities[j]
                    args2[j] = capacities[j]
                    dfs(*args2)
                else:
                    args2[i] = 0
                    args2[j] = args[i] + args[j]
                    dfs(*args2)

    dfs(0, 0, capacities[2])

    pos_c_fin = sorted(list(pos_c))
    for k in range(len(pos_c_fin)):
        if k > 0:
            fo.write(" ")
        fo.write(str(pos_c_fin[k]))
    fo.write("\n")
