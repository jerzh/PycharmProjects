"""
ID: jeremy.11
LANG: PYTHON3
TASK: prefix
"""
fi = open('prefix.in')
with open('prefix.out', 'w') as fo:
    primitives = []
    new_primitives = []
    while '.' not in new_primitives:
        primitives += new_primitives
        new_primitives = fi.readline().split()

    p_dict = dict.fromkeys(primitives)

    sequence = ''
    while True:
        line = fi.readline().strip()
        if not line:
            break
        sequence += line

    # dynamic programming: prefix len k composable?
    composable = [True]
    k = 1
    while k < 10 or any(composable[k - 10: k]) and k <= len(sequence):
        composable.append(any([composable[k - i] and sequence[k - i: k] in p_dict
                              for i in range(1, min(11, k + 1))]))
        k += 1

    # if k hits the end of the sequence
    if k == len(sequence) + 1:
        last_k = k - 11
        for i in range(k - 10, k):
            if composable[i]:
                last_k = i
        fo.write(str(last_k) + '\n')
    else:
        fo.write(str(k - 11) + '\n')
