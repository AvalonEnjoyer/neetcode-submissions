# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # postorder is left, right, root. preorder is root, left, right
        # using a preorder algorithm to go to the right node instead gives us root, right, left
        # this reversed become left, right, root

        res = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.right
            else:
                cur = stack.pop().left

        res.reverse()
        return res