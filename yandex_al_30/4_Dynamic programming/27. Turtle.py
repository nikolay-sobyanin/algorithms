n, m = map(int, input().split())

table = [[0] * (m + 1)]
for _ in range(n):
    table.append([0] + list(map(int, input().split())))

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + table[i][j]

print(dp[n][m])

i, j = n, m
ans = []
while i != 1 or j != 1:
    prev = dp[i][j] - table[i][j]

    if dp[i - 1][j] == prev:
        ans.append('D')
        i -= 1
    else:
        ans.append('R')
        j -= 1

print(*ans[::-1])


