import sys
sys.setrecursionlimit(1500)

with open('input.txt', 'r') as file:
    n, m = map(int, file.readline().strip().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        v_1, v_2 = map(int, file.readline().strip().split())
        graph[v_1].append(v_2)
        graph[v_2].append(v_1)


visited = [0] * (n + 1)


def dfs(graph, visited, now):
    visited[now] = 1
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig)


dfs(graph, visited, 1)

ans = [i for i in range(len(visited)) if visited[i] == 1]

print(len(ans))
print(*ans)

