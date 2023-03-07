n = int(input())
graph = [[] for _ in range(n + 1)]
distance = [-1] * (n + 1)
prev = [-2] * (n + 1)

for i in range(1, n + 1):
    arr = list(map(int, input().split()))
    for j in range(1, n + 1):
        if arr[j - 1] == 1:
            graph[i].append(j)

start, end = map(int, input().split())


def search_way(g, d, p, start_v, end_v):

    if start_v == end_v:
        return 0

    d[start_v] = 0
    p[start_v] = -1
    queue = [start_v]
    found_end = False
    while queue:
        now = queue[0]
        for neig in g[now]:
            if d[neig] == -1:
                d[neig] = d[now] + 1
                prev[neig] = now
                queue.append(neig)

            if neig == end_v:
                found_end = True
        queue.pop(0)

        if found_end:
            break

    if found_end:
        ans = []
        now = end_v
        while True:
            ans.append(now)
            now = p[now]
            if now == -1:
                return d[end_v], ans[::-1]
    else:
        return -1


path = search_way(graph, distance, prev, start, end)

if path in [0, -1]:
    print(path)
else:
    print(path[0])
    print(*path[1])


