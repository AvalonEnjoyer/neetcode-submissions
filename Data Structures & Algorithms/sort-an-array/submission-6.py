class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if len(nums)==1:
            return nums
        left = self.sortArray(nums[n//2:])
        right = self.sortArray(nums[:n//2])

        i,j,k=0,0,0

        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                nums[k]=left[i]
                k+=1
                i+=1
            else:
                nums[k]=right[j]
                k+=1
                j+=1

        while i<len(left):
            nums[k]=left[i]
            i+=1
            k+=1
        
        while j<len(right):
            nums[k]=right[j]
            j+=1
            k+=1

        return nums
        


