def search_diploma(folders: list) -> int:
	"""Algorithm complexity == O(N)"""
	return sum(folders) - max(folders) if len(folders) > 1 else 0


assert search_diploma([1, 2]) == 1
assert search_diploma([1, 2, 3, 10]) == 6
assert search_diploma([10]) == 0

with open('input.txt', 'r') as file:
	file.readline()
	folders = list(map(int, file.readline().strip().split()))

with open('output.txt', 'w') as file:
	file.write(str(search_diploma(folders)))
