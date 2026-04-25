class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for char in path.split("/"):
            if char == "..":
                if res:
                    res.pop()
            elif char!="" and char!=".":
                    res.append(char)
        return "/"+"/".join(res)