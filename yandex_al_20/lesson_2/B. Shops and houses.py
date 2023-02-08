def max_dist(d: list) -> int:
	dists = [0] * len(d)
	ans = 0
	shoppos = float('-inf')
	
	for i in range(len(d)):
		if d[i] == 2:
			shoppos = i
		if d[i] == 1:
			dists[i] = i - shoppos
	
	shoppos = float('inf')
	for i in range(len(d) - 1, -1, -1):
		if d[i] == 2:
			shoppos = i
		if d[i] == 1:
			min_dist = min(shoppos - i, dists[i])
			ans = max(ans, min_dist)
	return ans


d = list(map(int, input().split()))
print(max_dist(d))
