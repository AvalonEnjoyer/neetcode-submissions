class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        def backtrack(cur, idx):
            res.append(cur.copy())
            for i in range(idx,n):
                if i>idx and nums[i-1]==nums[i]:
                    continue
                cur.append(nums[i])
                backtrack(cur, i+1)
                cur.pop()
                            
        backtrack([],0)
        return res