"""
ID: jeremy.11
LANG: PYTHON3
TASK: sort3
"""
fi = open('sort3.in')
with open('sort3.out', 'w') as fo:
    n = int(fi.readline())
    unsorted = [int(s) for s in fi.readlines()]

    count = [0, 0, 0]
    for a in unsorted:
        count[a - 1] += 1

    misplaced = [[0] * 3 for i in range(3)]
    for i in range(n):
        if i < count[0]:
            misplaced[0][unsorted[i] - 1] += 1
        elif i < count[0] + count[1]:
            misplaced[1][unsorted[i] - 1] += 1
        else:
            misplaced[2][unsorted[i] - 1] += 1

    # two-way swap first
    total = 0
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        diff = min(misplaced[i][j], misplaced[j][i])
        total += diff
        misplaced[i][j] -= diff
        misplaced[j][i] -= diff
        misplaced[i][i] += diff
        misplaced[j][j] += diff

    # remaining three-way swaps
    total += 2 * max(misplaced[0][1], misplaced[0][2])

    fo.write(str(total) + '\n')
