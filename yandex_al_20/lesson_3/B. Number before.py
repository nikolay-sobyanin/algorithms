def number_before(arr: list):
    num_set = set()
    for num in arr:
        if num in num_set:
            print('YES')
        else:
            print('NO')
            num_set.add(num)


a = list(map(int, input().split()))
number_before(a)
