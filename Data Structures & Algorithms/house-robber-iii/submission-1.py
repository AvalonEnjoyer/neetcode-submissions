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
        
        memo = {None:0}

        def dfs(node):
            if node in memo:
                return memo[node]

            memo[node] = node.val
            
            if node.left:
                memo[node] += dfs(node.left.left)+dfs(node.left.right)
            if node.right:
                memo[node] += dfs(node.right.left)+dfs(node.right.right)
            memo[node] = max(memo[node], dfs(node.right)+dfs(node.left))
            return memo[node]

        return dfs(root)