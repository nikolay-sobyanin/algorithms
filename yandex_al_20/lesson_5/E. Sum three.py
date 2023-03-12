def read_arr():
    x = list(map(int, input().strip().split()))[1:]
    for i in range(len(x)):
        x[i] = x[i], i
    x.sort()
    return x


s = int(input().strip())
a = read_arr()
b = read_arr()
c = read_arr()

c.sort(key=lambda x: (x[0], -x[1]))

flag = False
for a_val, a_pos in a:
    c_pos = len(c) - 1
    for b_val, b_pos in b:
        while c_pos > 0 and a_val + b_val + c[c_pos][0] > s:
            c_pos -= 1

        if a_val + b_val + c[c_pos][0] == s and (not flag or (a_pos, b_pos, c_pos) < ans):
            ans = a_pos, b_pos, c[c_pos][1]
            flag = True

if flag:
    print(*ans)
else:
    print(-1)
