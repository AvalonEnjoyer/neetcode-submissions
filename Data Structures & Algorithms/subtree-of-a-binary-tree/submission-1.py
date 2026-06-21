# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.check_common(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or 
        self.isSubtree(root.right, subRoot))

    def check_common(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        if tree1 and tree2 and tree1.val == tree2.val:
            left = self.check_common(tree1.left, tree2.left)
            right = self.check_common(tree1.right, tree2.right)
            return left and right
        return False