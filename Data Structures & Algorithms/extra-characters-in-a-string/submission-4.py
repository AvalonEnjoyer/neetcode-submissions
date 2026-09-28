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
        dp = [0]*(n+1)
        
        for i in range(n-1, -1, -1):
            dp[i]=1+dp[i+1]
            cur = trie.root
            for j in range(i, n):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.is_word:
                    dp[i] = min(dp[i], dp[j+1])
        
        return dp[0]
        
