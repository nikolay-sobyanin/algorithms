def count_postfix():
    s = input().strip().split()
    stack = []
    for elem in s:
        if elem.isdigit():
            stack.append(int(elem))
            continue

        if elem == '+':
            n_1 = stack.pop()
            n_2 = stack.pop()
            stack.append(n_2 + n_1)
        elif elem == '*':
            n_1 = stack.pop()
            n_2 = stack.pop()
            stack.append(n_2 * n_1)
        elif elem == '-':
            n_1 = stack.pop()
            n_2 = stack.pop()
            stack.append(n_2 - n_1)
    return stack[0]


print(count_postfix())
