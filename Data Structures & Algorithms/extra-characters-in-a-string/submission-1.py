class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_word(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=Node()
            cur = cur.children[c]
        cur.is_word = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.add_word(word)

        n = len(s)
        dp = {n:0}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = 1+dfs(i+1)
            
            cur = trie.root

            for j in range(i, n):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.is_word:
                    res = min(res, dfs(j+1))
            dp[i]=res
            return res

        return dfs(0)
        
