# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [root]
        heights = {None:0} # {Node: Height}
        while stack:
            node = stack[-1]
            if node.left and node.left not in heights:
                stack.append(node.left)
            elif node.right and node.right not in heights:
                stack.append(node.right)
            else:
                node = stack.pop()

                leftHeight, rightHeight = heights[node.left], heights[node.right]
                if abs(rightHeight-leftHeight)>1:
                    return False
                heights[node] = 1+max(leftHeight, rightHeight)

        return True