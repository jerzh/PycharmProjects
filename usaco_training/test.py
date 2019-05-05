"""
ID: jeremy.11
LANG: PYTHON2
TASK: test
"""
fi = open("test.in")
with open("test.out", "w") as fo:
    x, y = map(int, fi.readline().split())
    z = x + y
    fo.write(str(z) + "\n")
