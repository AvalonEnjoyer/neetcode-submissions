# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS Solution
        res = []

        q = collections.deque()
        q.append(root)
        
        while q:
            level_res = []
            q_len = len(q)

            for i in range(q_len):
                node = q.popleft()
                if node:
                    level_res.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level_res:
                res.append(level_res)
        return res