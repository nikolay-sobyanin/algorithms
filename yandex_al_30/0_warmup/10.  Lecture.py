word = input()

ans = {}

for i, sym in enumerate(word, 1):
    if sym not in ans:
        ans[sym] = 0

    ans[sym] += i * (len(word) - i + 1)

for key in sorted(ans.keys()):
    print(key, ': ', ans[key], sep='')


