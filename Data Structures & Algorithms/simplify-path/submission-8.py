class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        components=path.split("/")
        for char in components:
            if char == "..":
                if res:
                    res.pop()
            elif char and char!=".":
                    res.append(char)
        return "/"+"/".join(res)