class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict = set(wordDict)
        n = len(s)

        def backtrack(idx, temp):
            if idx == n:
                res.append(temp[:-1])
                return 

            i = idx+1
            while i<=n:
                if s[idx:i] in wordDict:
                    backtrack(i, temp+s[idx:i]+" ")
                i+=1
        backtrack(0, "")
        return res

