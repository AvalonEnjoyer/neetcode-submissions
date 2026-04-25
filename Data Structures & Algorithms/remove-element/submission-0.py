class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[j] == val:
                nums.remove(nums[j])
            else:
                j += 1
        return len(nums)