def cub(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d


with open('cubroot.in', 'r') as file:
    params = list(map(int, file.readline().strip().split()))
    r = 1
    while cub(r, *params) * cub(-r, *params) >= 0:
        r *= 2
    l = -r

    while r - l > 0.000001:
        x = (l + r) / 2
        if cub(x, *params) * cub(r, *params) > 0:
            r = x
        else:
            l = x


with open('cubroot.out', 'w') as file:
    file.write(str(l))
