def init_mem(size):
    memory = []
    for i in range(size):
        key, left_son, right_son = 0, i + 1, 0
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


mem = init_mem(10)
new_node(mem)
new_node(mem)
new_node(mem)
del_node(mem, 1)

print(mem[1])
print(*mem[0], sep='\n')




