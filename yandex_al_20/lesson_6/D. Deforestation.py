a, k, b, m, x = map(int, input().strip().split())

l = 0
r = x * 2 // a + 1

while l < r:
    days = (l + r) // 2
    hd = days // k
    hf = days // m
    lumber = (days - hd) * a + (days - hf) * b
    if lumber < x:
        l = days + 1
    else:
        r = days

print(l)
