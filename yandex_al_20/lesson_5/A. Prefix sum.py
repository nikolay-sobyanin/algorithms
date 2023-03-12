n, q = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
prefix_sum = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]


for _ in range(q):
    l, r = map(int, input().strip().split())
    res = prefix_sum[r] - prefix_sum[l - 1]
    print(res)
