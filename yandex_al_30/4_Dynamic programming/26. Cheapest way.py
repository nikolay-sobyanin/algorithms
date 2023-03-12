n, m = map(int, input().split())

table = [[0] * (m + 1)]
for _ in range(n):
    table.append([0] + list(map(int, input().split())))

dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
dp[0][1] = dp[1][0] = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + table[i][j]

print(dp[n][m])
