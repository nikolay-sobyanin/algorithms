n = int(input())

graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for i in range(1, n + 1):
    arr = list(map(int, input().split()))
    for j in range(1, n + 1):
        if arr[j - 1] == 1:
            graph[i].append(j)


def search_cycle(g, p, now):
    stack = [[now, 0]]
    p[now] = -1
    cycle_found = False

    while stack:
        v = stack[-1]
        flag = True
        for i in range(v[1], len(g[v[0]])):
            neig = g[v[0]][i]
            if p[neig] == 0:
                flag = False
                v[1] = i + 1
                p[neig] = v[0]
                stack.append([neig, 0])
                break
            if p[v[0]] != neig:
                cycle_start = neig
                cycle_found = True
                break

        if cycle_found:
            break
        if flag:
            stack.pop()

    if cycle_found:
        ans = []
        while True:
            node = stack.pop()
            ans.append(node[0])
            if node[0] == cycle_start:
                break
        return ans
    else:
        return None


is_cycle = False
for i in range(1, len(parent)):
    if parent[i] == 0:
        cycle = search_cycle(graph, parent, i)
        if cycle:
            is_cycle = True
            print('YES')
            print(len(cycle))
            print(*cycle)
            break

if not is_cycle:
    print('NO')



