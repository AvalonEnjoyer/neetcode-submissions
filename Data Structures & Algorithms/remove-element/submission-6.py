class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,k=0,0
        n = len(nums)-1
        while i <= n-k:
            if nums[i] == val:
                nums.pop(i)
                k+=1
            else:
                i+=1
        print(nums)
        res = len(nums)
        return res