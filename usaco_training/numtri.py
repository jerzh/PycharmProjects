"""
ID: jeremy.11
LANG: PYTHON2
TASK: numtri
"""
fi = open("numtri.in")
with open("numtri.out", "w") as fo:
    r = int(fi.readline())
    lines = []
    for line in fi:
        lines.append(line.strip("\n"))
    prev_sums = None
    for i in xrange(r, 0, -1):
        sums = map(int, lines[i - 1].split())
        if prev_sums is not None:
            for j in xrange(len(sums)):
                sums[j] += max(prev_sums[j], prev_sums[j + 1])
        prev_sums = sums
    fo.write(str(prev_sums[0]) + "\n")
