bin_tree = []


def search_tree(tree, x):
    if len(tree) == 0:
        return False
    key, left, right = tree
    if x == key:
        return True
    elif x < key:
        if not left:
            return False
        else:
            return search_tree(left, x)
    elif x > key:
        if not right:
            return False
        else:
            return search_tree(right, x)


def add_tree(tree, x):
    if len(tree) == 0:
        tree.append(x)
        tree.append([])
        tree.append([])
        return
    key, left, right = tree
    if x < key:
        add_tree(left, x)
    elif x > key:
        add_tree(right, x)


def print_tree(tree, depth=0):
    key, left, right = tree

    if left:
        print_tree(left, depth + 1)
    print('.' * depth + str(key))

    if right:
        print_tree(right, depth + 1)


with open('input.txt', 'r') as file:
    for line in file.readlines():
        text = line.strip().split()
        cmd = text[0]

        if cmd == 'ADD':
            n = int(text[1])
            if search_tree(bin_tree, n):
                print('ALREADY')
            else:
                add_tree(bin_tree, n)
                print('DONE')
        elif cmd == 'SEARCH':
            n = int(text[1])
            if search_tree(bin_tree, n):
                print('YES')
            else:
                print('NO')
        elif cmd == 'PRINTTREE':
            print_tree(bin_tree)

