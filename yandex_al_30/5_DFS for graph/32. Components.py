# from threading import stack_size
# from sys import setrecursionlimit
#
#
# setrecursionlimit(1000000)
# stack_size(134217728)


with open('input.txt', 'r') as file:
    n, m = map(int, file.readline().strip().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        v_1, v_2 = map(int, file.readline().strip().split())
        graph[v_1].append(v_2)
        graph[v_2].append(v_1)

visited = [0] * (n + 1)


def dfs_no_recursive(color, now):
    stack = [now]
    while stack:
        node = stack.pop()
        visited[node] = color

        for neig in graph[node]:
            if not visited[neig]:
                stack.append(neig)


color = 0
for i in range(1, len(visited)):
    if not visited[i]:
        color += 1
        dfs_no_recursive(color, i)


components = [[] for _ in range(color + 1)]
for i in range(1, len(visited)):
    components[visited[i]].append(i)

print(len(components) - 1)
for i in range(1, len(components)):
    print(len(components[i]))
    print(*components[i])
