n = int(input())

dp = [0] * (n + 1)
prev = [0] * (n + 1)

dp[0] = 0
dp[1] = 0
prev[0] = 0
prev[1] = 1

for i in range(2, n + 1):
    tmp = []
    if i % 3 == 0:
        tmp.append((dp[i // 3], i // 3))
    if i % 2 == 0:
        tmp.append((dp[i // 2], i // 2))

    tmp.append((dp[i - 1], i - 1))
    min_prev = min(tmp, key=lambda x: x[0])
    dp[i] = min_prev[0] + 1
    prev[i] = min_prev[1]

ans = []
tmp = n
while not tmp == 1:
    ans.append(tmp)
    tmp = prev[tmp]

ans.append(1)

print(dp[n])
print(*ans[::-1])


