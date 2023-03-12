n = int(input())
graph = [[] for _ in range(n + 1)]
distance = [-1] * (n + 1)

for i in range(1, n + 1):
    arr = list(map(int, input().split()))
    for j in range(1, n + 1):
        if arr[j - 1] == 1:
            graph[i].append(j)

start, end = map(int, input().split())


def search_path(g, d, v_start, v_end):
    d[v_start] = 0
    queue = [v_start]
    while queue:
        now = queue[0]
        for neig in g[now]:
            if d[neig] == -1:
                d[neig] = d[now] + 1
                queue.append(neig)

            if neig == v_end:
                return d[v_end]
        queue.pop(0)
    return -1


print(search_path(graph, distance, start, end))
