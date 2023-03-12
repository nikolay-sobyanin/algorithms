k = int(input())
x_min = y_min = x_max = y_max = None

for _ in range(k):
    x, y = map(int, input().split())
    if x_min is None:
        x_min = x_max = x
        y_min = y_max = y

    x_min = min(x, x_min)
    x_max = max(x, x_max)
    y_min = min(y, y_min)
    y_max = max(y, y_max)


print(x_min, y_min, x_max, y_max)

