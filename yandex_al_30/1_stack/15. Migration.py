def migration():
    input()
    val = list(map(int, input().strip().split()))
    stack = []
    ans = [-1] * len(val)

    for i in range(len(val)):
        if not stack:
            stack.append((val[i], i))
            continue

        if stack[-1][0] <= val[i]:
            stack.append((val[i], i))
            continue

        flag = True
        while flag:
            _, num = stack.pop()
            ans[num] = i
            if not stack or stack[-1][0] <= val[i]:
                stack.append((val[i], i))
                flag = False
    print(' '.join(map(str, ans)))


migration()
