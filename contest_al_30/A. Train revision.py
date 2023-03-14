n = int(input())

train = []
wagons = {}


def add(count, name):
    if name not in wagons:
        wagons[name] = 0
    wagons[name] += count
    train.append([count, name])


def delete(count):
    while count > 0 and len(train) > 0:
        if train[-1][0] <= count:
            wag = train.pop()
            count -= wag[0]
            wagons[wag[1]] -= wag[0]
        else:
            train[-1][0] -= count
            wagons[train[-1][1]] -= count
            break


def get(name):
    if name in wagons:
        return wagons[name]
    else:
        return 0


for _ in range(n):
    line = input().split()
    cmd = line[0]

    if cmd == 'add':
        add(int(line[1]), line[2])
    elif cmd == 'delete':
        delete(int(line[1]))
    elif cmd == 'get':
        print(get(line[1]))
