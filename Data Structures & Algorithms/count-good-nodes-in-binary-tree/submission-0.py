# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global good 
        good = 0 # root node is always a valid node
        cur_max = float('-inf')

        def dfs(node, cur_max):
            if not node:
                return
            if cur_max <= node.val:
                global good 
                good += 1
                cur_max = node.val
            dfs(node.left, cur_max)
            dfs(node.right, cur_max)

        dfs(root, cur_max)
        return good
