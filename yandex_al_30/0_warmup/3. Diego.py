n = int(input())
diego = set(map(int, input().split()))
k = int(input())
collectors = list(map(int, input().split()))

diego = list(diego)
diego.sort()


def search(arr, p):
    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        if arr[0] < p:
            return 1
        else:
            return 0

    l = 0
    r = len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] >= p:
            r = m
        else:
            l = m + 1

    if l == len(arr) - 1:
        if arr[l] < p:
            return len(arr)
        else:
            return len(arr) - 1

    if l == 0:
        if arr[l] >= p:
            return 0
        else:
            return 1

    return l


for p in collectors:
    print(search(diego, p))
