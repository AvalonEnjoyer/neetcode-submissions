# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(tree1, tree2):
            if not tree2:
                return True
            if not tree1:
                return False
            # Preorder traversal
            if check_common(tree1, tree2):
                return True
            left = dfs(tree1.left, tree2)
            right = dfs(tree1.right, tree2)
            return left or right

        def check_common(tree1, tree2):
            if not tree1 and not tree2:
                return True
            # elif tree1 and not tree2:
            #     return False
            if tree1 and tree2 and tree1.val == tree2.val:
                left = check_common(tree1.left, tree2.left)
                right = check_common(tree1.right, tree2.right)
                return left and right
            return False
            
        return dfs(root, subRoot)