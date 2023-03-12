pi = 3.141592653589793

n = int(input())
r1_max = 0
r2_min = float('inf')

events = []
for i in range(1, n + 1):
    r1, r2, phi_1, phi_2 = map(float, input().split())
    r1_max = max(r1_max, r1)
    r2_min = min(r2_min, r2)

    events.append((phi_1, -i))
    events.append((phi_2, i))

events.sort()
used = set()
cnt = 0
for event in events:
    if event[1] < 0:
        used.add(-event[1])
        cnt += 1
    elif event[1] in used:
        cnt -= 1

ans = 0
for i in range(len(events)):
    event = events[i]
    if event[1] < 0:
        cnt += 1
    else:
        cnt -= 1

    if cnt == n:
        if i < len(events) - 1:
            ans += (events[i + 1][0] - events[i][0]) * (r2_min ** 2 - r1_max ** 2) / 2
        else:
            ans += (events[0][0] - events[len(events) - 1][0] + 2 * pi) * (r2_min ** 2 - r1_max ** 2) / 2

print(ans)
