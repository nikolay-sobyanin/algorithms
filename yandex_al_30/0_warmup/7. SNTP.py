a = list(map(int, input().split(':')))
b = list(map(int, input().split(':')))
c = list(map(int, input().split(':')))


def convert_sec(time):
    return (time[0] * 60 + time[1]) * 60 + time[2]


a_sec = convert_sec(a)
b_sec = convert_sec(b)
c_sec = convert_sec(c)

if c_sec < a_sec:
    delta = (24*60*60) + c_sec - a_sec
else:
    delta = c_sec - a_sec

if delta % 2 == 0:
    delta //= 2
else:
    delta = delta // 2 + 1

now_time = b_sec + delta

if now_time > (24*60*60):
    now_time -= (24*60*60)

s = now_time % 60
now_time //= 60
m = now_time % 60
h = now_time // 60

ans = []
for i in (h, m, s):
    if i // 10 == 0:
        ans.append('0' + str(i))
    else:
        ans.append(str(i))

print(':'.join(ans))


