n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]


for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] != b[j - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        else:
            dp[i][j] = 1 + dp[i - 1][j - 1]


ans = []
i = n
j = m
while j != 0 and i != 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        ans.append(a[i - 1])
        i -= 1
        j -= 1

print(*ans[::-1])

