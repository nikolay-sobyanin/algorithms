n, m = map(int, input().split())

events = list([(int(pos), 0) for pos in input().split()])
for i in range(1, m + 1):
    l, r = map(int, input().split())
    events.append((l, -1, i))
    events.append((r, 1, i))

events.sort()
ans = {}
cats = 0
for event in events:
    if event[1] == -1:
        ans[event[2]] = cats
    elif event[1] == 1:
        ans[event[2]] = cats - ans[event[2]]
    elif event[1] == 0:
        cats += 1


for key in sorted(ans.keys()):
    print(ans[key])
