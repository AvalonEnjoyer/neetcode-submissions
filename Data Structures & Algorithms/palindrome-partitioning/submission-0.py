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

        def backtrack(j, i):
            if i>=len(s):
                if i == j:
                    res.append(cur.copy())
                return

            if substring_palindrome_check(j,i):
                cur.append(s[j:i+1])
                backtrack(i+1,i+1)
                cur.pop()
            
            backtrack(j,i+1)

        backtrack(0, 0)
        return res