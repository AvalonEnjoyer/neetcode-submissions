# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # parent or child can be selected
            # both can be skipped if the child of child has better values 
        # cannot be consecutive depth
        # can skip nodes on one depth if the previous one
        def dfs(node):
            if not node:
                return (0,0)

            left = dfs(node.left)
            right = dfs(node.right)
            
            rooted = node.val+left[1]+right[1]
            unrooted = max(left)+max(right)
            return (rooted,unrooted)

        return max(dfs(root))