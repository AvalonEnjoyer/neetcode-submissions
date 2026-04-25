class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = 0
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    count+=1
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums