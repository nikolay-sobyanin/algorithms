n, k = map(int, input().split())

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    pos = i - 1
    tmp = 0
    while pos >= 0 and i - pos <= k:
        tmp += dp[pos]
        pos -= 1

    dp[i] = tmp

print(dp[n - 1])


