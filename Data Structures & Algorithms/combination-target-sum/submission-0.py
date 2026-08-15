class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def dfs(i, temp, summa):
            if summa==target:
                res.append(temp.copy())
                return
            
            if i>=len(nums) or summa>target:
                return

            temp.append(nums[i])
            dfs(i,temp,summa+nums[i])
            temp.pop()
            dfs(i+1, temp, summa)

        dfs(0,[],0)
        return res