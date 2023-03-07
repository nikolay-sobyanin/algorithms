n, m, s, t, q = map(int, input().split())
field = [[-1] * m for _ in range(n)]

fleas = []
for _ in range(q):
    fleas.append(tuple(map(int, input().split())))


def adjacent_cells(row, col, n, m):
    def in_field(row, col, n, m):
        return (0 <= row < n) and (0 <= col < m)

    moves = [
        (-2, 1),
        (-1, 2),
        (1, 2),
        (2, 1),
        (2, -1),
        (1, -2),
        (-1, -2),
        (-2, -1),
    ]
    adj_cells = []
    for step_i, step_j in moves:
        cell = (row + step_i, col + step_j)
        if in_field(cell[0], cell[1], n, m):
            adj_cells.append(cell)
    return adj_cells


is_finish = False
k = 0

distance = [[(s - 1, t - 1)]]
field[s - 1][t - 1] = k

while not is_finish:
    distance.append([])
    for cell in distance[k]:
        for adj_cell in adjacent_cells(cell[0], cell[1], n, m):
            if field[adj_cell[0]][adj_cell[1]] == -1:
                distance[k + 1].append(adj_cell)
                field[adj_cell[0]][adj_cell[1]] = k + 1

    k += 1
    if not distance[k]:
        is_finish = True


def cnt_ans(field, fleas):
    ans = 0
    for cell in fleas:
        row, col = cell[0] - 1, cell[1] - 1
        if field[row][col] == -1:
            return -1
        else:
            ans += field[row][col]

    return ans


print(cnt_ans(field, fleas))
