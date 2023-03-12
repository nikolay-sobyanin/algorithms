n = int(input())
costs = [0]
k = 0

for _ in range(n):
    cost = int(input())
    if cost > 100:
        k += 1
    costs.append(cost)

dp = [[float('inf')] * (k + 3) for _ in range(len(costs))]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(k + 1):
        if costs[i] > 100:
            dp[i][j] = min(dp[i - 1][j - 1] + costs[i], dp[i - 1][j + 1])
        else:
            dp[i][j] = min(dp[i - 1][j] + costs[i], dp[i - 1][j + 1])


j_coupon = 0
tmp_min = float('inf')
for j in range(k,  -1, -1):
    if dp[n][j] < tmp_min:
        j_coupon = j
        tmp_min = dp[n][j]


days = []
j = j_coupon
for i in range(n, 0, -1):
    if dp[i][j] == dp[i - 1][j + 1]:
        j += 1
        days.append(i)
    else:
        if costs[i] > 100:
            j -= 1

print(dp[n][j_coupon])
print(j_coupon, len(days))
print(*days[::-1], sep='\n')
