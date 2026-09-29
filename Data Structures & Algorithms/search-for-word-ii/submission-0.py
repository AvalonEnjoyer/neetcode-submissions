class Node():
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie():
    def __init__(self):
        self.root = Node()
    
    def add_word(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.add_word(word)

        res, visited = set(), set()
        m = len(board)
        n = len(board[0])

        def backtrack(r, c, cur, word):
            if (r<0 or c<0 or r>=m or c>=n or (r,c) in visited or board[r][c] not in cur.children):
                return
            
            visited.add((r,c))
            cur = cur.children[board[r][c]]
            word+= board[r][c]

            if cur.is_word:
                res.add(word)

            backtrack(r+1,c,cur,word)
            backtrack(r-1,c,cur,word)
            backtrack(r,c+1,cur,word)
            backtrack(r,c-1,cur,word)

            visited.remove((r,c))

        for i in range(m):
            for j in range(n):
                backtrack(i,j, trie.root, "")

        return list(res)