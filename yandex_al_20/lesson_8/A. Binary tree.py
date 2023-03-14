tree = []


def search_tree(tree, n):
    if len(tree) == 0:
        return False

    if n == tree[0]:
        return True
    elif n < tree[0]:
        if search_tree(tree[1], n):
            return True
        else:
            return False
    elif tree[0] < n:
        if search_tree(tree[2], n):
            return True
        else:
            return False


def add_tree(tree, n):
    if len(tree) == 0:
        tree.append(n)
        tree.append([])
        tree.append([])
        return

    if n < tree[0]:
        add_tree(tree[1], n)
    elif n > tree[0]:
        add_tree(tree[2], n)


def print_tree():
    pass


with open('input.txt', 'r') as file:
    for line in file.readlines():
        text = line.strip().split()
        cmd = text[0]

        if cmd == 'ADD':
            n = int(text[1])
            if search_tree(tree, n):
                print('ALREADY')
            else:
                add_tree(tree, n)
                print('DONE')
        elif cmd == 'SEARCH':
            n = int(text[1])
            if search_tree(tree, n):
                print('YES')
            else:
                print('NO')
        elif cmd == 'PRINTTREE':
            print_tree()

