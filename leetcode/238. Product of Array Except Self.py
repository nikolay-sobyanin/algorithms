from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums))
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        postfix = [1] * (len(nums))
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        return [postfix[i] * prefix[i] for i in range(len(nums))]


solution = Solution()

assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert solution.productExceptSelf([1, 1, 1, 1]) == [1, 1, 1, 1]
assert solution.productExceptSelf([0, 0, 0]) == [0, 0, 0]
