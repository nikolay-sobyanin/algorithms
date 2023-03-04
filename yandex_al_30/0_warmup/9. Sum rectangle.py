n, m, k = map(int, input().split())

ps = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, len(row) + 1):
        ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + row[j - 1]


def count_sum(prefix_sum, x1, y1, x2, y2):
    ans = prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]
    return ans


for _ in range(k):
    coord = map(int, input().split())
    print(count_sum(ps, *coord))
