first = list(map(int, input().strip().split()))
second = list(map(int, input().strip().split()))


i = 0
flag = True
while first and second and flag:
    f = first.pop(0)
    s = second.pop(0)

    if f == 0 and s == 9:
        first.extend([f, s])
    elif s == 0 and f == 9:
        second.extend([f, s])
    elif f > s:
        first.extend([f, s])
    else:
        second.extend([f, s])

    i += 1
    if i == 10**6:
        flag = False

if not flag:
    print('botva')
else:
    if first:
        print('first', i)
    else:
        print('second', i)
