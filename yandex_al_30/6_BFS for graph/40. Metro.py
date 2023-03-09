n = int(input())
m = int(input())
graph = [[] for _ in range(n + m + 1)]
visited = [-1] * (n + m + 1)

for i in range(n + 1, n + m + 1):
    stations = list(map(int, input().split()))[1:]
    graph[i].extend(stations)
    for station in stations:
        graph[station].append(i)

start, end = map(int, input().split())
# print(*graph[1:n + 1], sep='\n')
# print()
# print(*graph[n + 1:], sep='\n')

k = 0
transfers = [[]]
for line in graph[start]:
    visited[line] = k
    for station in graph[line]:
        visited[station] = k
        transfers[k].append(station)


while transfers[k]:
    transfers.append([])
    for station in transfers[k]:
        for line in graph[station]:
            if visited[line] == -1:
                visited[line] = k + 1
                for st in graph[line]:
                    if visited[st] == -1:
                        visited[st] = k + 1
                        transfers[k + 1].append(st)

    k += 1

print(visited[end])

