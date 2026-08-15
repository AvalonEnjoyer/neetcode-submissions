class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(i, temp, summa):
            if summa == target:
                res.append(temp.copy())
                return
            for j in range(i, n):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if summa+candidates[j]>target:
                    break

                temp.append(candidates[j])
                backtrack(j+1, temp, summa+candidates[j])
                temp.pop()

        backtrack(0,[],0)
        return res
