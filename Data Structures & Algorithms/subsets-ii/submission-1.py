class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        prev_idx = idx = 0

        for i in range(len(nums)):
            idx = prev_idx if i>=1 and nums[i]==nums[i-1] else 0
            prev_idx = len(res)
            for j in range(idx, prev_idx):
                temp = res[j].copy()
                temp.append(nums[i])
                res.append(temp)
        return res