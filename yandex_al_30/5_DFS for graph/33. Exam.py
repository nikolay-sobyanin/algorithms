with open('input.txt', 'r') as file:
    n, m = map(int, file.readline().strip().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        v_1, v_2 = map(int, file.readline().strip().split())
        graph[v_1].append(v_2)
        graph[v_2].append(v_1)

visited = [0] * (n + 1)


def dfs_paint(color, now):
    visited[now] = color
    for neig in graph[now]:
        if visited[neig] == color:
            return False
        elif visited[neig] == 0:
            dfs_paint(3 - color, neig)
    return True


flag = True
for i in range(1, len(visited)):
    if not visited[i]:
        flag = dfs_paint(1, i)
        if not flag:
            break


if flag:
    print('YES')
else:
    print('NO')

