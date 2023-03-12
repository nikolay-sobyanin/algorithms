def sort_wagons():
    input()
    path_1 = list(map(int, input().strip().split()))
    path_2 = []
    deadlock = []
    next_wagon = 1
    while path_1:
        deadlock.append(path_1.pop(0))
        flag = True
        while flag:
            if deadlock and deadlock[-1] == next_wagon:
                path_2.append(deadlock.pop())
                next_wagon += 1
            else:
                flag = False

    return False if deadlock else True


print('YES' if sort_wagons() else 'NO')
