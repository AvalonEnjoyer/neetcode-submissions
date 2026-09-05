class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def substring_palindrome_check(start, end):
            while start<end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True

        def backtrack(i):
            if i==len(s):
                res.append(cur.copy())
                return

            for j in range(i, len(s)):
                if substring_palindrome_check(i,j):
                    cur.append(s[i:j+1])  
                    backtrack(j+1)
                    cur.pop()
            
        backtrack(0)
        return res