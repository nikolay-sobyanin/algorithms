k = int(input())
s = input()

alphabet = set(s)

ans = 0
for sym in alphabet:
    tmp_k = k
    right = 0
    for left in range(len(s)):
        while right < len(s) and tmp_k >= 0:
            if s[right] == sym:
                right += 1
            else:
                if tmp_k > 0:
                    tmp_k -= 1
                    right += 1
                else:
                    break

        ans = max(ans, right - left)

        if s[left] != sym:
            tmp_k += 1

print(ans)
