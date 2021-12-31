"""
ID: jeremy.11
LANG: PYTHON3
TASK: runround
"""
fi = open('runround.in')
with open('runround.out', 'w') as fo:
    n = int(fi.readline())

    # apparently you aren't supposed to brute force this one lol
    # (but I'm glad I tried brute forcing it anyway)
    # the idea is to generate all numbers with distinct digits, since there
    # are 9! + 8! + ... of them and that number is small enough

    def calc_digits(a):
        digits = []
        while a > 0:
            digits.insert(0, a % 10)
            a //= 10
        return digits

    def is_runaround(digits):
        visited = [False] * len(digits)
        current = 0
        while not visited[current]:
            visited[current] = True
            current = (current + digits[current]) % len(digits)
        return current == 0 and all(visited)

    n += 1  # start with number higher than n
    cur_digits = calc_digits(n)
    while 0 in cur_digits or len(set(cur_digits)) != len(cur_digits)\
            or not is_runaround(cur_digits):
        n += 1
        cur_digits = calc_digits(n)

    fo.write(str(n) + '\n')
