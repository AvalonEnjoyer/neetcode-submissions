# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = ""
        q = deque([root])

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                if node=="x":
                    res+="x "
                    continue
                res+=f"{node.val} "

                q.append(node.left) if node.left else q.append("x")
                q.append(node.right) if node.right else q.append("x")
        print(res)
        return res
                
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data=="":
            return
        data = data.split(" ")
        n = len(data)-1
        i=0
        print(data, n)

        def create(index):
            if index >= n:
                return None
            root = TreeNode(index)
            root.left = create(index+1)
            root.right = create(index+2)
            return root
            
        return root

        