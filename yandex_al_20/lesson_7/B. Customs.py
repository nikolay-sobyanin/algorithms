n = int(input())
events = []
for _ in range(n):
    t, l = map(int, input().split())
    events.append((t, 1))
    events.append((t + l, -1))

events.sort()
ans = 0
occupied = 0

for event in events:
    if event[1] == 1:
        occupied += 1
    elif event[1] == -1:
        occupied -= 1
    ans = max(ans, occupied)

print(ans)
