class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i]<= n and nums[i] != nums[nums[i] - 1]:
                correct = nums[i]-1
                nums[i], nums[correct] = nums[correct], nums[i]
        for i in range(1, n+1):
            if i != nums[i-1]:
                return i
        return n+1