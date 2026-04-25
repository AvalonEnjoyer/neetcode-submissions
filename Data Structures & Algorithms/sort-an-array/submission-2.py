class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            lowest_index = i
            for j in range(i+1, n):
                if nums[j] < nums[lowest_index]:
                    lowest_index = j
            nums[i], nums[lowest_index] = nums[lowest_index], nums[i]
        return nums