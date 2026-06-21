# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node):
            if not node:
                return (True, 0)
            left_is_balanced, lHeight = check_height(node.left)
            right_is_balanced, rHeight = check_height(node.right)
            if abs(rHeight - lHeight)  <= 1 and left_is_balanced and right_is_balanced:
                balanced = True
            else:
                balanced = False
            return (balanced, 1 + max(lHeight,rHeight))

        return check_height(root)[0]