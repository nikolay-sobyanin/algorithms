# Link: https://contest.yandex.ru/contest/28730/problems/E/


def search_point(d: int, x: int, y: int) -> int:
	if (x >= 0) and (y >= 0) and (x + y <= d):
		return 0
	
	vertices = [(0, 0), (d, 0), (0, d)]
	tmp_length = float('inf')
	near_vertex = None
	for vertex, point_vertex in enumerate(vertices, 1):
		length = ((point[0] - point_vertex[0])**2 + (point[1] - point_vertex[1])**2)**0.5
		if length < tmp_length:
			tmp_length = length
			near_vertex = vertex
	return near_vertex


def optimal_search_point(d: int, x: int, y: int) -> int:
	if (x >= 0) and (y >= 0) and (x + y <= d):
		return 0
	dist = [(x**2 + y**2, 1), ((x - d)**2 + y**2, 2), (x**2 + (y - d)**2, 3)]
	return min(dist)[1]


d = int(input())
point = tuple(map(int, input().split()))
print(search_point(d, *point))

