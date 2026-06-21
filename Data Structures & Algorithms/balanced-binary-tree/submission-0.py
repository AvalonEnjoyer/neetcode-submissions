# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balanced = True

        def check_height(node):
            if not node:
                return 0 
            lHeight = check_height(node.left)
            rHeight = check_height(node.right)
            if abs(rHeight - lHeight) > 1:
                nonlocal balanced
                balanced = False
            return 1+max(lHeight, rHeight)

        check_height(root)
        return balanced