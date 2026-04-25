class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1 # at least 1 unique element
        n = len(nums)
        i = 0
        j = 1
        while j < n:
            if nums[i] == nums[j]:
                j+=1
            else:
                i+=1
                k+=1
                nums[i] = nums[j]
        return k