from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = {}
        for i in range(len(nums)):
            if target - nums[i] in prev_nums:
                return [i, prev_nums[target - nums[i]]]
            else:
                prev_nums[nums[i]] = i
