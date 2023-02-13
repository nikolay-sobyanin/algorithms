def count_equal(a: list, b: list) -> int:
    """Algorithm complexity == O(N)"""
    return len(set(a) & set(b))


assert count_equal([1, 3, 2], [1, 2, 4]) == 2

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(count_equal(a, b))
