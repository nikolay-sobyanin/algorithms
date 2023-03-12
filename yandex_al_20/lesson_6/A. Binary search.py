n = int(input())
x = list(map(int, input().split()))
x.sort()

k = int(input())


def l_search(arr, p):
    l = 0
    r = len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] >= p:
            r = m
        else:
            l = m + 1
    return l


def r_search(arr, p):
    l = 0
    r = len(arr) - 1
    while l < r:
        m = (l + r + 1) // 2
        if arr[m] <= p:
            l = m
        else:
            r = m - 1
    return l


def search(arr, a, b):
    if len(arr) == 1:
        if a <= arr[0] <= b:
            return 1
        else:
            return 0

    left = l_search(arr, a)
    right = r_search(arr, b)

    if left == right:
        if a <= arr[left] <= b:
            return 1
        else:
            return 0
    else:
        return r_search(arr, b) - l_search(arr, a) + 1


ans = []
for _ in range(k):
    a, b = map(int, input().split())
    ans.append(search(x, a, b))

print(*ans)
