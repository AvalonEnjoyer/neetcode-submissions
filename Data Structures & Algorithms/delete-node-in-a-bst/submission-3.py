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
                    return prev,node
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
            elif not node.left:
                return node.right
            else:
                temp = node.left
                cur = node.right
                
                while cur.left:
                    cur = cur.left
                cur.left = temp

                return node.right

        prev, to_delete = findNode(None, root)
        if not to_delete:
            return root
        
        print(f"previous value {prev.val if prev else None}, to delete: {to_delete.val}, key:{key}")
        # new_head = rearrange(to_delete)

        # Replace the reference to to_delete from the original tree and replace it with newHead
        if prev==None:
            root = rearrange(to_delete)
        else:
            if prev.left and prev.left.val == to_delete.val:
                prev.left = rearrange(to_delete)
            else:
                prev.right = rearrange(to_delete)

        return root

        
            