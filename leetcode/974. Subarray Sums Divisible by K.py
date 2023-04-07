from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        # Остатки от деления на k
        m = [0] * k
        m[0] = 1
        for x in prefix_sum:
            m[x % k] += 1

        ans = 0
        for x in m:
            ans += x * (x - 1) // 2

        return ans


solution = Solution()
print(solution.subarraysDivByK([4,5,0,-2,-3,1], 5))
