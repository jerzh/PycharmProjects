"""
ID: jeremy.11
LANG: PYTHON2
TASK: ariprog
"""
# rip i've been cheesed apparently python is too slow
# I coded the same thing in java and it passed
fi = open("ariprog.in")
with open("ariprog.out", "w") as fo:
    n = int(fi.readline())
    m = int(fi.readline())
    max_seq = 2 * m * m
    none = True

    bisquares = [False] * (max_seq + 1)
    for p in xrange(m + 1):
        for q in xrange(p + 1):
            bisquares[p * p + q * q] = True

    # def bisquare(num):
    #     if num % 4 == 3:
    #         return False
    #     for p in xrange(int(math.ceil(math.sqrt(num / 2))), min(int(math.sqrt(num)), m) + 1):
    #         for q in xrange(p + 1):
    #             if p * p + q * q == num:
    #                 return True
    #     return False

    # for b in xrange(1, max_seq / (n - 1) + 1):
    #     if n >= 4 and b % 4 != 0:
    #         continue
    #     for a in xrange(max_seq - b * (n - 1) + 1):
    #         valid = True
    #         for i in xrange(n):
    #             if not bisquare(a + b * i):
    #                 valid = False
    #                 break
    #         if valid:
    #             none = False
    #             fo.write(str(a) + " " + str(b) + "\n")

    for b in xrange(1, max_seq // (n - 1) + 1):
        if n >= 4 and b % 4 != 0:
            continue
        # print "b: " + str(b)
        pos_a = set()
        for a in xrange(b):
            count = 0
            for a1 in range(a, max_seq + 1, b):
                # print "a1: " + str(a1)
                if not bisquares[a1]:
                    count = 0
                else:
                    count += 1
                    if count >= n:
                        none = False
                        pos_a.add(a1 - b * (n - 1))
        for a in pos_a:
            fo.write(str(a) + " " + str(b) + "\n")

    if none:
        fo.write("NONE" + "\n")
