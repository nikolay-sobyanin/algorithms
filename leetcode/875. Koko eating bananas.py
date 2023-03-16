from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            cnt_hrs = 0
            for pile in piles:
                cnt_hrs += ((pile - 1) // mid) + 1  # округление вверх

            if cnt_hrs <= h:
                right = mid
            else:
                left = mid + 1
        return left


solution = Solution()
ans = solution.minEatingSpeed([3,6,7,11], 8)
print(ans)
