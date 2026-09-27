class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}
        res = []

        def backtrack(temp,idx):
            if len(temp)==len(digits):
                res.append("".join(temp))
                return
            for char in mapping[digits[idx]]:
                temp.append(char)
                backtrack(temp, idx+1)
                temp.pop()
        
        if not digits:
            return res
        backtrack([],0)
        print(res)
        return res