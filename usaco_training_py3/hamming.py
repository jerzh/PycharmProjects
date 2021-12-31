"""
ID: jeremy.11
LANG: PYTHON3
TASK: hamming
"""
fi = open('hamming.in')
with open('hamming.out', 'w') as fo:
    n, b, d = [int(s) for s in fi.readline().split()]

    def binary_sum(x):
        total = 0
        while x > 0:
            total += x % 2
            x //= 2
        return total

    def hamming_dist(x, y):
        return binary_sum(x ^ y)

    codewords = [0]
    while len(codewords) < n:
        for trial in range(2 ** b):
            if all([hamming_dist(trial, w) >= d for w in codewords]):
                codewords.append(trial)
                break

    for i in range((len(codewords) - 1) // 10 + 1):
        fo.write(' '.join(map(str, codewords[10 * i: 10 * (i + 1)])) + '\n')
