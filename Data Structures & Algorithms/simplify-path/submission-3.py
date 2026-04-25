class Solution:
    def simplifyPath(self, path: str) -> str:
        path_marker = "/"
        res = []
        for char in path.split("/"):
            if char:
                if char == "..":
                    if res:
                        res.pop()
                elif char == ".":
                    continue
                else:
                    res.append(char)
        return path_marker+"/".join(res)