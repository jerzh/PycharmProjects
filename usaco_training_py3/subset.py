"""
ID: jeremy.11
LANG: PYTHON3
TASK: subset
"""
fi = open('subset.in')
with open('subset.out', 'w') as fo:
    n = int(fi.readline())

    if (n * (n + 1) // 2) % 2 != 0:
        fo.write('0\n')
    else:
        # dynamic programming! consider # ways to get any sum
        dp = [[0] * ((i + 1) * (i + 2) // 2 + 1) for i in range(n)]
        dp[0][0] = 1
        dp[0][1] = 1
        for i in range(1, n):
            for j in range((i + 1) * (i + 2) // 2 + 1):
                if 0 <= j - (i + 1):
                    dp[i][j] += dp[i - 1][j - (i + 1)]
                if j <= i * (i + 1) // 2:
                    dp[i][j] += dp[i - 1][j]
        fo.write(str(dp[n - 1][n * (n + 1) // 4] // 2) + '\n')
