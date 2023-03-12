def l_bin_search(arr, param):
    left = 0
    right = len(arr) - 1

    while left < right:
        middle = (left + right) // 2
        if arr[middle] >= param:
            right = middle
        else:
            left = middle + 1
    return left if arr[left] == param else -1


def r_bin_search(arr, param):
    left = 0
    right = len(arr) - 1

    while left < right:
        middle = (left + right + 1) // 2
        if arr[middle] <= param:
            left = middle
        else:
            right = middle - 1
    return left if arr[left] == param else -1


input()
arr = list(map(int, input().strip().split()))
arr.sort()
input()
search_num = map(int, input().strip().split())

for num in search_num:
    left = l_bin_search(arr, num) + 1
    right = r_bin_search(arr, num) + 1
    print(left, right)
