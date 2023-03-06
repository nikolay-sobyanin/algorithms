n, m = map(int, input().split())
discovered = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def dfs_paint(g, d, color, now):
    d[now] = color
    for neig in g[now]:
        if d[neig] == 0:
            if not dfs_paint(g, d, 3 - color, neig):
                return False

        if d[neig] == d[now]:
            return False

    return True


flag = True
for i in range(1, len(discovered)):
    if discovered[i] == 0:
        if not dfs_paint(graph, discovered, 1, i):
            flag = False
            break


print('YES' if flag else 'NO')
