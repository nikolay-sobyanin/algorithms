n = int(input())

a, b, c = [float('inf')], [float('inf')], [float('inf')]

for _ in range(n):
    l = list(map(int, input().split()))
    a.append(l[0])
    b.append(l[1])
    c.append(l[2])

a.append(float('inf'))
a.append(float('inf'))
b.append(float('inf'))
b.append(float('inf'))
c.append(float('inf'))
c.append(float('inf'))

dp = [0] * (n + 3)

for i in range(1, n + 1):
    dp[i] = min(dp[i - 1] + a[i], dp[i - 2] + b[i - 1], dp[i - 3] + c[i - 2])

print(dp[n])

