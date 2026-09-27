class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []

        def backtrack(idx, temp):
            if len(temp)==len(digits):
                res.append(temp)
                return
            for char in mapping[digits[idx]]:
                backtrack(idx+1, temp+char)
        
        if not digits:
            return res
        backtrack(0, "")
        return res