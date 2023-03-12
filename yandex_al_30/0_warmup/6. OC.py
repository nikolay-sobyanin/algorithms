input()
m = int(input())

arr = []
ans = [1] * m
for _ in range(m):
    a, b = map(int, input().split())
    arr.append((a, b))

for i in range(m):
    for j in range(i - 1, -1, -1):
        if arr[i][0] <= arr[j][1] and arr[j][0] <= arr[i][1]:
            ans[j] = 0

print(sum(ans))

