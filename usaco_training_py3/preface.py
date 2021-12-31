"""
ID: jeremy.11
LANG: PYTHON3
TASK: preface
"""
fi = open('preface.in')
with open('preface.out', 'w') as fo:
    n = int(fi.readline())

    final = [0] * 9

    for i in range(n + 1):
        digits = []
        while i > 0:
            digits.append(i % 10)
            i //= 10
        mapping = {0: (0, 0, 0), 1: (1, 0, 0), 2: (2, 0, 0), 3: (3, 0, 0), 4: (1, 1, 0),
                   5: (0, 1, 0), 6: (1, 1, 0), 7: (2, 1, 0), 8: (3, 1, 0), 9: (1, 0, 1)}
        for d in range(len(digits)):
            partial = mapping[digits[d]]
            final[2 * d + 0] += partial[0]
            final[2 * d + 1] += partial[1]
            final[2 * d + 2] += partial[2]

    letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    for i in range(7):
        if final[i] > 0:
            fo.write(' '.join([letters[i], str(final[i])]) + '\n')
