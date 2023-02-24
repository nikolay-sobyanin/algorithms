n = int(input())

if n < 3:
    dp = [0] * 4
else:
    dp = [0] * (n + 1)

dp[0] = 1
dp[1] = 2
dp[2] = 4
dp[3] = 7
for i in range(4, n + 1):
    dp[i] = 2 * dp[i - 1] - dp[i - 4]

print(dp[n])
