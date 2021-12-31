"""
ID: jeremy.11
LANG: PYTHON3
TASK: frac1
"""
fi = open('frac1.in')
with open('frac1.out', 'w') as fo:
    n = int(fi.readline())

    # calculate gcd, assume a < b
    def gcd(a, b):
        if a > 0:
            return gcd(b % a, a)
        else:
            return b

    big_list = []
    for i in range(n + 1):
        for j in range(i + 1):
            if gcd(j, i) == 1:
                big_list.append((j, i))

    big_list = sorted(big_list, key=lambda x: x[0]/x[1])

    for s in map(lambda x: f'{x[0]}/{x[1]}', big_list):
        fo.write(s + '\n')
