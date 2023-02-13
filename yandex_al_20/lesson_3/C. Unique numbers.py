def count_unique_numbers(arr: list) -> list:
    unique_numb = []
    for i in range(len(arr)):
        if arr.count(arr[i]) == 1:
            unique_numb.append(arr[i])

    return unique_numb


a = [int(x) for x in input().split()]
ans = ' '.join(map(str, count_unique_numbers(a)))
print(ans)

