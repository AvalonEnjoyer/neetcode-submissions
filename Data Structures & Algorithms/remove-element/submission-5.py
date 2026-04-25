class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=1
        i=0
        n = len(nums)
        while i <= n-k:
            if nums[i] == val:
                nums.pop(i)
                k+=1
            else:
                i+=1
        print(nums)
        res = len(nums)
        return res