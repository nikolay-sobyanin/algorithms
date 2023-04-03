from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = [0] * len(nums)
        for i in range(len(nums)):
            if counts[nums[i]] == 0:
                counts[nums[i]] += 1
            else:
                return nums[i]

    def findDuplicate_2(self, nums: List[int]) -> int:
        for num in nums:
            nums[abs(num) - 1] *= -1
            if nums[abs(num) - 1] > 0:
                return abs(num)


solutions = Solution()

assert solutions.findDuplicate([1, 2, 1]) == 1
assert solutions.findDuplicate([1, 2, 3, 3, 4, 5]) == 3
