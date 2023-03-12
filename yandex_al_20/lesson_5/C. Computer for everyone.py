n, m = map(int, input().strip().split())
groups = sorted([(val, i) for i, val in enumerate(map(int, input().strip().split()))])
audiences = sorted([(val, i) for i, val in enumerate(map(int, input().strip().split()))])

p = 0
ans = [0] * n

pos_a = m - 1
for i in range(n - 1, -1, -1):
    if pos_a >= 0 and groups[i][0] + 1 <= audiences[pos_a][0]:
        ans[groups[i][1]] = audiences[pos_a][1] + 1
        pos_a -= 1
        p += 1


print(p)
print(' '.join(map(str, ans)))
