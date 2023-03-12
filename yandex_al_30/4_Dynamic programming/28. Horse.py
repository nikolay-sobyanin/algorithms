n, m = map(int, input().split())

ind = 2
dp = [[0] * (m + ind) for _ in range(n + ind)]

dp[0][1] = 1
for i in range(ind, n + ind):
    for j in range(ind, m + ind):
        dp[i][j] = dp[i - 2][j - 1] + dp[i - 1][j - 2]

print(dp[n + ind - 1][m + ind - 1])

