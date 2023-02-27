n = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr = [0] + arr

dp = [(0, 0), (float('inf'), 0)]


for i in range(2, n + 1):
    dp.append(
        (min(dp[i - 1][0], dp[i - 1][1]) + (arr[i] - arr[i - 1]), dp[i - 1][0])
    )

print(arr)
print(dp)
print(dp[n][0])
