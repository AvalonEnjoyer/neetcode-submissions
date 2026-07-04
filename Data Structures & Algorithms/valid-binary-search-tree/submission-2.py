# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, left, right):
            if not node:
                return True
            if left < node.val < right:
                left_valid = isValid(node.left, left, node.val)
                right_valid = isValid(node.right, node.val, right)
                return left_valid and right_valid
            else:
                return False

        return isValid(root, float("-inf"), float("inf") )