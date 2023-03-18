from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        visited = set()

        def in_grid(x, y):
            return 0 <= x < m and 0 <= y < n

        def bfs(i, j):
            queue = []
            visited.add((i, j))
            queue.append((i, j))
            while queue:
                row, column = queue.pop(0)
                adjacent_cells = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dx, dy in adjacent_cells:
                    if in_grid(row + dx, column + dy) and grid[row + dx][column + dy] == '1':
                        if (row + dx, column + dy) not in visited:
                            visited.add((row + dx, column + dy))
                            queue.append((row + dx, column + dy))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    ans += 1
                    bfs(i,j)
        return ans


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
solution = Solution()
answer = solution.numIslands(grid)
print(answer)
