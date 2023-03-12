n = int(input())
events = []

for i in range(n):
    l, r = map(int, input().split())
    events.append((l, 1))
    events.append((r, -1))

events.sort()
ans = 0
occupied = 0
for i in range(len(events)):
    if occupied > 0:
        ans += events[i][0] - events[i - 1][0]

    if events[i][1] == -1:
        occupied -= 1
    elif events[i][1] == 1:
        occupied += 1

print(ans)
