def cost(s: str) -> int:
	"""Algorithm complexity == O(N)"""
	l = len(s)
	if (l == 0) or (l == 1):
		return 0
	
	ans = 0
	if len(s) % 2 != 0:
		center = l // 2
		for i in range(1, l // 2 + 1):
			if s[center - i] != s[center + i]:
				ans += 1
	else:
		center_r = l // 2
		center_l = center_r - 1
		for i in range(0, l // 2):
			if s[center_l - i] != s[center_r + i]:
				ans += 1
	return ans


assert cost('') == 0
assert cost('a') == 0
assert cost('acbca') == 0
assert cost('acca') == 0
assert cost('acbcd') == 1
assert cost('accv') == 1
assert cost('abcde') == 2


s = input()
print(cost(s))
