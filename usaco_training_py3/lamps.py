"""
ID: jeremy.11
LANG: PYTHON3
TASK: lamps
"""
fi = open('lamps.in')
with open('lamps.out', 'w') as fo:
    n = int(fi.readline())
    c = int(fi.readline())
    on = [int(s) - 1 for s in fi.readline().split()[:-1]]
    off = [int(s) - 1 for s in fi.readline().split()[:-1]]

    # only 8 distinct possibilities
    # b1 = [1] * 6
    # b2 = [(i + 1) % 2 for i in range(6)]
    # # b3 = b1 ^ b2  <- this also gets rid of parity for the most part
    # b4 = [int(i % 3 == 0) for i in range(6)]
    #
    # binary = []
    # for i in range(8):
    #     temp = []
    #     for j in range(3):
    #         temp.append(i % 2)
    #         i //= 2
    #     binary.append(temp)
    #
    # poss = sorted([[b[0] & b1[j] ^ b[1] & b2[j] ^ b[2] & b4[j]
    #                 for j in range(6)] for b in binary])

    # hard-coding this is just easier (lamps, smallest c, 2nd smallest c)
    poss = [([0, 0, 0, 0, 0, 0], 1, 2), ([0, 0, 1, 1, 1, 0], 2, 3),
            ([0, 1, 0, 1, 0, 1], 1, 2), ([0, 1, 1, 0, 1, 1], 1, 3),
            ([1, 0, 0, 1, 0, 0], 2, 3), ([1, 0, 1, 0, 1, 0], 1, 2),
            ([1, 1, 0, 0, 0, 1], 2, 3), ([1, 1, 1, 1, 1, 1], 0, 2)]

    on = set([lamp % 6 for lamp in on])
    off = set([lamp % 6 for lamp in off])

    possible = False
    for p in poss:
        if all([p[0][lamp] == 1 for lamp in on])\
                and all([p[0][lamp] == 0 for lamp in off])\
                and (c == p[1] or c >= p[2]):
            possible = True
            p_ext = (p[0] * (n // 6 + 1))[:n]
            fo.writelines(map(str, p_ext))
            fo.write('\n')
    if not possible:
        fo.write('IMPOSSIBLE\n')
