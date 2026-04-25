class Solution:
    import re
    def encode(self, strs: List[str]) -> str:
        length = len(strs)
        concatenated_str = ""
        for i, string in enumerate(strs):
            if i == 0:
                concatenated_str = "_" + str(len(string)) + "#" + string
            else:
                concatenated_str += "_" + str(len(string)) + "#" + string
        return concatenated_str


    def decode(self, s: str) -> List[str]:
        return re.split(pattern=r"_+\d+#", string=s)[1:]


## Solution 1 - 100% runtime and 95.4% memory
# class Solution: 
#     def encode(self, strs: List[str]) -> str:
#         length = len(strs)
#         if length == 0:
#             return "null"
#         concatenated_str = str.join("__", strs)
#         return concatenated_str


#     def decode(self, s: str) -> List[str]:
#         if s == "null":
#             return []
#         return s.split("__")
