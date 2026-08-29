class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, n = [], len(nums)

        def dfs(i):
            if i==len(nums):
                res.append(nums.copy())
                return
            
            for j in range(i, n):
                if j>i and nums[j]==nums[i]:
                    continue
                nums[i], nums[j]=nums[j], nums[i]
                dfs(i+1)

            for j in range(n-1, i, -1):
                nums[j],nums[i]=nums[i], nums[j]
            
        dfs(0)
        return res