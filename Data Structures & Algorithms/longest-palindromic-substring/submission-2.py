class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res_len, res_idx = 0,0

        for i in range(n):
            # even palindromes
            l,r = i,i
            while l>=0 and r<n and s[l]==s[r]:
                if r-l+1 > res_len:
                    res_idx = l
                    res_len = r-l+1
                l-=1 
                r+=1
            
            # odd palindromes
            l,r = i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                if r-l+1 > res_len:
                    res_idx = l
                    res_len = r-l+1
                l-=1
                r+=1 
        
        print(res_idx, res_len)
        return s[res_idx:res_idx+res_len]