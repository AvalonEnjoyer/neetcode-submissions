class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        elif len(strs[0]) == 1:
            return strs[0]
        # Base comparisons on the smallest word
        min_len = min(len(str) for str in strs)

        def check_common_prefix(index):
            # Check if every string's character matches up to the given index
            for i in range(1,len(strs)):
                for j, char in enumerate(strs[i][:index]):
                    if char != strs[0][j]:
                        return False
            return True
        low = 1
        high = min_len
        while low<=high:
            mid = (high+low)//2
            if check_common_prefix(mid):
                low += 1
            else:
                high -= 1
        return strs[0][:high]