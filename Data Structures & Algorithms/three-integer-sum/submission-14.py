class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        i = 0
        while i<n-2:
            k = n-1
            j = i+1
            while j<k:
                if nums[j]+nums[k] == -nums[i]:
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    k-=1
                if nums[j]+nums[k] < -nums[i]:
                    j+=1
                else:
                    k-=1
            i+=1
        return res
