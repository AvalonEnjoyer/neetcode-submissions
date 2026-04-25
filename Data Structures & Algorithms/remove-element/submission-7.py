class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,k=0,len(nums)-1
        while i <= k:
            print(nums, i, k)
            if nums[k] == val:
                nums.pop() # remove last element if it is equal to val
                k-=1
            elif nums[i] == val:
                nums.pop(i)
                k-=1
            else:
                i+=1
        return len(nums)