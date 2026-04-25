class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for char in path.split("/"):
            if char and char!=".":
                if char != "..":
                    res.append(char)
                else:
                    if res:
                        res.pop()
        return "/"+"/".join(res)