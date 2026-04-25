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

        # Set up another binary search
        pivot_point = l
        if pivot_point == 0:
            r = len(nums)-1
            l = 0
        elif nums[-1]>=target:
            r = len(nums)-1
            l = pivot_point
        else:
            r = pivot_point-1
            l = 0
        
        print(l, r)
        while l<=r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                return mid
        return -1
