class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,k=0,len(nums)-1
        while i <= k:
            if nums[i] == val:
                nums[i]=nums[k] # move known non-value int to index with value
                nums.pop() # delete last value
                k-=1
            else:
                i+=1
        return len(nums)