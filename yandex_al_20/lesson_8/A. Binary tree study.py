def init_mem(size):
    memory = []
    for i in range(size):
        key, left_son, right_son = 0, -1, -1
        memory.append([key, left_son, right_son])
    free = 0
    return [memory, free]


def new_node(mem_str):
    memory, free = mem_str
    mem_str[1] = memory[free][1]
    return free


def del_node(mem_str, index):
    memory, free = mem_str
    memory[index][1] = free
    mem_str[1] = index


def find(mem_str, root, x):
    key = mem_str[0][root][0]
    if key == x:
        return root
    elif x < root:
        left = mem_str[0][root][1]
        if left == -1:
            return -1
        else:
            return find(mem_str, left, x)
    elif x > root:
        right = mem_str[0][root][2]
        if right == -1:
            return -1
        else:
            return find(mem_str, right, x)


def crt_fill(mem_str, key):
    index = new_node(mem_str)
    mem_str[0][index][0] = key
    mem_str[0][index][1] = -1
    mem_str[0][index][2] = -1
    return index


def add(mem_str, root, x):
    key = mem_str[0][root][0]
    if x < key:
        left = mem_str[0][root][1]
        if left == -1:
            mem_str[0][root][1] = crt_fill(mem_str, x)
        else:
            add(mem_str, left, x)
    elif x > key:
        right = mem_str[0][root][2]
        if right == -1:
            mem_str[0][root][2] = crt_fill(mem_str, x)
        else:
            add(mem_str, right, x)


max_nodes = 10
memory_structure = init_mem(max_nodes)
add(memory_structure, 0, 10)




