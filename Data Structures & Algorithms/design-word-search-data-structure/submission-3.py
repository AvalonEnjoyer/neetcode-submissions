class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root=Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.root

        def dfs(root, i):
            if i>=len(word):
                if root.is_word:
                    return True
                return False
            if word[i]!=".":
                if word[i] not in root.children:
                    return False
                return dfs(root.children[word[i]],i+1)
            for key in root.children.keys():
                if dfs(root.children[key], i+1):
                    return True
            return False
            # while searching need to look for next char in ith idx or all spaces where "." could fit
            
        return dfs(cur, 0)
            

