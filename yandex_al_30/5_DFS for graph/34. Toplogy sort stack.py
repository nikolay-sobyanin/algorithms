n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)


def check_cycle(g, v, now):
    stack = [[now, 0, len(g[now])]]
    v[now] = 1

    while stack:
        node = stack[-1]
        flag = True

        for i in range(node[1], node[2]):
            neig = g[node[0]][i]
            if v[neig] == 1:
                return True
            elif v[neig] == 0:
                v[neig] = 1
                node[1] = i + 1

                flag = False
                stack.append([neig, 0, len(g[neig])])
                break

        if flag:
            visited[node[0]] = 2
            stack.pop()

    return False


def topology_sort(g, v, a, now):
    stack = [[now, 0, len(g[now])]]

    while stack:
        node = stack[-1]

        flag = True
        for i in range(node[1], node[2]):
            neig = g[node[0]][i]
            if v[neig] == 0:
                node[1] = i + 1
                flag = False
                stack.append([neig, 0, len(g[neig])])
                break

        if flag:
            v[node[0]] = 2
            a.append(node[0])
            stack.pop()


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
