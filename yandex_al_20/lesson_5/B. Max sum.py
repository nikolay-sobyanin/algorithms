n = int(input().strip())
arr = list(map(int, input().strip().split()))


def maxsum(iterable):
    maxsofar = maxendinghere = 0

    all_negative = True
    for x in iterable:
        if x >= 0:
            all_negative = False

        maxendinghere = max(maxendinghere + x, 0)
        maxsofar = max(maxsofar, maxendinghere)

    if all_negative:
        return max(iterable)
    return maxsofar


print(maxsum(arr))
