# Link: https://contest.yandex.ru/contest/28730/problems/C/


def check_date(x: int, y: int, z: int) -> int:
	if (1 <= x <= 12) and (1 <= y <= 12):
		return 1 if x == y else 0
	else:
		return 1


assert check_date(1, 1, 2000) == 1
assert check_date(1, 2, 2000) == 0
assert check_date(20, 1, 2000) == 1
assert check_date(12, 11, 2000) == 0


x, y, z = map(int, input().split())
print(check_date(x, y, z))



