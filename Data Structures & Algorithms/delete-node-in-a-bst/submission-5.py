# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return

        def findNode(prev, node):
            if node:
                if node.val==key:
                    # Rearranging the subtree 
                    new_head = rearrange(node)
                    # Changing the reference to the new subtree
                    if prev: 
                        if prev.left and prev.left.val == key:
                            prev.left = new_head
                        else:
                            prev.right = new_head
                    return prev, new_head
                elif node.val<key:
                    return findNode(node, node.right)
                else:
                    return findNode(node, node.left)
            else:
                return prev, None

        # Rearrange the section of the tree after the to_delete node, if needed
        def rearrange(node):
            if not node.right:
                return node.left if node.left else None
            elif node.left:
                # Moving the left of the BST subtree to the leftmost node of the right subtree
                cur = node.right
                while cur.left:
                    cur = cur.left
                cur.left = node.left
            return node.right

        prev, new_head = findNode(None, root)

        return root if prev else new_head

        
            