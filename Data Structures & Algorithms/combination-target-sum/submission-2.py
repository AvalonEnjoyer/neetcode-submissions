class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()

        def dfs(i, temp, summa):
            if summa==target:
                res.append(temp.copy())
                return
            
            for j in range(i, len(nums)):
                if summa+nums[j]>target:
                    return
                temp.append(nums[j])
                dfs(j,temp, summa+nums[j])
                temp.pop()

        dfs(0,[],0)
        return res