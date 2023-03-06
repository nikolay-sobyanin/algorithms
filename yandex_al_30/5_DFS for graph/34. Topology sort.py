n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)


def check_cycle(g, v, now):
    v[now] = 1
    for neig in g[now]:
        if v[neig] == 0:
            if check_cycle(g, v, neig):
                return True
        if v[neig] == 1:
            return True
    v[now] = 2
    return False


def topology_sort(g, v, a, now):
    for neig in g[now]:
        if v[neig] == 0:
            topology_sort(g, v, a, neig)
    v[now] = 2
    a.append(now)


flag = False
for i in range(1, len(visited)):
    if visited[i] == 0:
        if check_cycle(graph, visited, i):
            flag = True
            break

if flag:
    print(-1)
else:
    visited = [0] * (n + 1)
    ans = []
    for i in range(1, len(visited)):
        if visited[i] == 0:
            topology_sort(graph, visited, ans, i)

    print(*ans[::-1])
