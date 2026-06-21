# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q:
            return False

        def dfs(node1, node2):
            if node1 and node2:
                if node1.val == node2.val:
                    left = dfs(node1.left, node2.left)
                    right = dfs(node1.right, node2.right)  
                    return True if left and right else False
                else:
                    return False
            elif node1 or node2:
                return False
            else:
                return True
        
        return dfs(p, q)