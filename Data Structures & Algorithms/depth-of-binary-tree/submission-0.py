# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0 
        
        def findDepth(node):
            if node:
                lDepth = findDepth(node.left) if node.left else 0
                rDepth = findDepth(node.right) if node.right else 0
                return 1+max(lDepth, rDepth)
            else:
                return 0

        depth = findDepth(root)
        return depth