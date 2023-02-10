def benches_legs(length_bench: int, legs: list) -> list:
	"""Algorithm complexity == O(K). K is count of legs"""
	center_bench = length_bench // 2
	
	if length_bench % 2 == 1:
		for i in range(len(legs)):
			if legs[i] == center_bench:
				return [legs[i]]
	
	for i in range(len(legs) - 1):
		if legs[i] <= center_bench <= legs[i + 1]:
			return [legs[i], legs[i + 1]]


assert benches_legs(5, [0, 2]) == [2]
assert benches_legs(14, [1, 6, 8, 11, 12, 13]) == [6, 8]
assert benches_legs(10, [1, 2, 4, 5, 9]) == [4, 5]

with open('input.txt', 'r') as file:
	length_bench, _ = map(int, file.readline().strip().split())
	legs = list(map(int, file.readline().strip().split()))

with open('output.txt', 'w') as file:
	s = ' '.join(map(str, benches_legs(length_bench, legs)))
	file.write(s)
