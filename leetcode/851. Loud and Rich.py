from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for a, b in richer:
            graph[b].append(a)

        answer = [0] * n
        for x in range(n):
            visited = set()
            y = x
            stack = [[x, 0]]  # [node, pos]
            visited.add(x)

            while stack:
                node, pos = stack[-1]
                add_node = False
                for j in range(pos, len(graph[node])):
                    neig = graph[node][j]
                    if neig not in visited:
                        stack[-1][1] = j + 1
                        stack.append([neig, 0])
                        visited.add(neig)
                        if quiet[neig] < quiet[y]:
                            y = neig
                        add_node = True
                        break

                if not add_node:
                    stack.pop()

            answer[x] = y
        return answer


solution = Solution()
answer = solution.loudAndRich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0])
print(answer)

