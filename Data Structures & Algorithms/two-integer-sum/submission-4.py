class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement not in sum_map:
                sum_map[num] = i
            else:
                return [sum_map[complement], i]
        