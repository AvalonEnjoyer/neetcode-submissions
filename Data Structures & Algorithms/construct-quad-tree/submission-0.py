"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def dfs(n,r,c):
            if n==1:
                return Node(grid[r][c], True)

            n = n//2
            topleft = dfs(n,r,c)
            topright = dfs(n,r,c+n)
            bottomleft = dfs(n,r+n,c)
            bottomright = dfs(n,r+n,c+n)


            are_leaves = topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and bottomright.isLeaf
            same_value = (topleft.val == topright.val) and (topright.val == bottomleft.val) and (bottomleft.val == bottomright.val)
            print(same_value)
            return Node(topleft.val, True) if (are_leaves and same_value) else Node(0,False, topleft, topright, bottomleft, bottomright)

        return dfs(n,0,0)