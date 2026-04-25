class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        # Find the pivot point first
        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid

        pivot = l
        # Set up another binary search
        if nums[-1]>=target>=nums[pivot]:
            r = len(nums)-1
            l = pivot
        else:
            r = pivot-1
            l = 0
        
        while l<=r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                return mid
        return -1
