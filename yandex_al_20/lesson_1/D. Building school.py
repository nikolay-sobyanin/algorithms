# Link: https://contest.yandex.ru/contest/28730/problems/D/


def count_ways(coordinates: list) -> int:
	"""Count min sum ways. algorithm complexity == O(N**2)"""
	ways_min = float('inf')
	school_coord = 0
	for coord in range(coordinates[0], coordinates[-1] + 1):
		ways = 0
		for i in coordinates:
			ways += abs(i - coord)
		if ways <= ways_min:
			ways_min = ways
			school_coord = coord
	
	return school_coord


assert count_ways([1]) == 1
assert count_ways([1, 2]) == 2 or 1
assert count_ways([1, 2, 3, 4]) == 3 or 2
assert count_ways([-1, 0, 1]) == 0
assert count_ways([-4, -3, -2, -1]) == -2 or -3


def optimal_count_ways(n: int, coordinates: list) -> int:
	"""Count min sum ways. algorithm complexity == O(1)"""
	k = n // 2
	return coordinates[k]


assert optimal_count_ways(1, [1]) == 1
assert optimal_count_ways(2, [1, 2]) == 2 or 1
assert optimal_count_ways(4, [1, 2, 3, 4]) == 3 or 2
assert optimal_count_ways(3, [-1, 0, 1]) == 0
assert optimal_count_ways(4, [-4, -3, -2, -1]) == -2 or -3


n = int(input())
coordinates = list(map(int, input().split()))

print(optimal_count_ways(n, coordinates))
