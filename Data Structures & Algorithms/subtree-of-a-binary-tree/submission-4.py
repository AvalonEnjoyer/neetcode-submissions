# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # pre-order traversal
        def traverse(tree1, tree2):
            if not tree2:
                return True
            if not tree1:
                return False
            if isSame(tree1, tree2): 
                return True
            left = traverse(tree1.left, tree2)
            right = traverse(tree1.right, tree2)
            return left or right

        def isSame(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if tree1 and tree2 and tree1.val==tree2.val:
                left = isSame(tree1.left, tree2.left)
                right = isSame(tree1.right, tree2.right)
                return left and right
            return False
        
        return traverse(root, subRoot)