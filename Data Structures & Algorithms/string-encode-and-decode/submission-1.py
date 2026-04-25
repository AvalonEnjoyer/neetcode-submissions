class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "null"
        concatenated_str = str.join("__", strs)
        return concatenated_str


    def decode(self, s: str) -> List[str]:
        if s == "null":
            return []
        return s.split("__")
