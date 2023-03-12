n = int(input())

plan = []
for k in range(n):
    input()
    plan.append([])
    for i in range(n):
        row = list(input().strip())
        plan[k].append(row)


def search_s(plan):
    for k in range(len(plan)):
        for i in range(len(plan[k])):
            for j in range(len(plan[k][i])):
                if plan[k][i][j] == 'S':
                    return k, i, j


def adjacent_cells(coord, plan):
    def in_field(coord, plan):
        n = len(plan)
        return (0 <= coord[0] < n) and (0 <= coord[1] < n) and (0 <= coord[2] < n)

    moves = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]
    adj_cells = []
    for step_k, step_i, step_j in moves:
        cell = (coord[0] + step_k, coord[1] + step_i, coord[2] + step_j)
        if in_field(cell, plan) and plan[cell[0]][cell[1]][cell[2]] == '.':
            adj_cells.append(cell)
    return adj_cells


k = 0
s = search_s(plan)
distance = [[s]]
plan[s[0]][s[1]][s[2]] = k
is_finish = False

while not is_finish:
    distance.append([])
    for cell in distance[k]:
        for adj_cell in adjacent_cells(cell, plan):
            distance[k + 1].append(adj_cell)
            plan[adj_cell[0]][adj_cell[1]][adj_cell[2]] = k + 1
            if adj_cell[0] == 0:
                is_finish = True
    k += 1

print(k)
