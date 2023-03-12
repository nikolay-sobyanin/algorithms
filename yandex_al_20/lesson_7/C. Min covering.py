m = int(input())
l, r = map(int, input().split())
segs = []
while l != 0 or r != 0:
    if r > 0 and l < m:
        segs.append((l, r))
    l, r = map(int, input().split())

segs.sort()
ans = []
now_r = 0
next_r = 0
now_best = 0, 0

for seg in segs:
    if seg[0] > now_r:
        ans.append(now_best)
        now_r = next_r
        if now_r >= m:
            break

    if seg[0] <= now_r and seg[1] > next_r:
        next_r = seg[1]
        now_best = seg

if now_r < m:
    now_r = next_r
    ans.append(now_best)

if now_r < m:
    print('No solution')
else:
    print(len(ans))
    for seg in ans:
        print(*seg)
