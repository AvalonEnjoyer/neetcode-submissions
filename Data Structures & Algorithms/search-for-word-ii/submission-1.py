class Node():
    def __init__(self):
        self.children = [None]*26
        self.idx = -1
        self.refs = 0

class Trie():
    def __init__(self):
        self.root = Node()
    
    def add_word(self, word, i):
        cur = self.root
        for c in word:
            idx = ord(c)-ord("a")
            if not cur.children[idx]:
                cur.children[idx] = Node()
            cur = cur.children[idx]
            cur.refs += 1
        cur.idx = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for i,word in enumerate(words):
            trie.add_word(word,i)

        m = len(board)
        n = len(board[0])
        res = []

        def get_idx(c):
            return ord(c)-ord("a")

        def backtrack(r, c, cur):
            if (r<0 or c<0 or r>=m or c>=n or 
                board[r][c]=="*" or 
                not cur.children[get_idx(board[r][c])]):
                return 0
            
            temp= board[r][c]
            board[r][c]= "*"
            prev = cur
            cur = cur.children[get_idx(temp)]
            found = 0

            if cur.idx != -1:
                res.append(words[cur.idx])
                cur.idx = -1
                found += 1

            found += backtrack(r+1,c,cur)
            found += backtrack(r-1,c,cur)
            found += backtrack(r,c+1,cur)
            found += backtrack(r,c-1,cur)

            board[r][c]=temp
            cur.refs -= found
            if not cur.refs:
                prev.children[get_idx(temp)]=None
            return found

        for i in range(m):
            for j in range(n):
                trie.root.refs -= backtrack(i,j,trie.root)

        return res