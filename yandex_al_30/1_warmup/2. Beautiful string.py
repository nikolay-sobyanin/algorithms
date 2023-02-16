# Необходима оптимизация. Не прошел последний тест на время.

def count_beautiful(k: int, s: str) -> int:
    if len(s) == 1:
        return 1
    if len(s) - 1 <= k:
        return len(s)

    ans = 0
    for i in range(len(s) - k - 1):
        j = i
        tmp_k = k
        tmp_ans = 0
        while j < len(s):
            if s[j] == s[i]:
                tmp_ans += 1
            else:
                if tmp_k > 0:
                    tmp_k -= 1
                    tmp_ans += 1
                else:
                    break
            j += 1
        if tmp_ans > ans:
            ans = tmp_ans
    return ans


assert count_beautiful(1, 'a') == 1
assert count_beautiful(3, 'ab') == 2
assert count_beautiful(2, 'abc') == 3
assert count_beautiful(2, 'abcaz') == 4
assert count_beautiful(2, 'helto') == 3
assert count_beautiful(0, 'aaccddd') == 3
assert count_beautiful(4, 'acadaddavcg') == 8

k = int(input())
s = input()

print(count_beautiful(k, s))
