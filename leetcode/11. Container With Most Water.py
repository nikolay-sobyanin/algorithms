from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area


solution = Solution()
assert solution.maxArea([1, 1]) == 1
assert solution.maxArea([3, 0]) == 0
assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

