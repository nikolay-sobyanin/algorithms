n = int(input())

ans = 0
arr = []
for _ in range(n):
    arr.append(int(input()))

for i in range(1, n):
    ans += min(arr[i], arr[i - 1])

print(ans)
