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
            str0, length = strs[0][:index], len(strs)-1
            return all(strs[i][:index]==str0 for i in range(1,len(strs)))

        low = 1
        high = min_len
        while low<=high:
            mid = (high+low)//2
            if check_common_prefix(mid):
                low += 1
            else:
                high -= 1
        return strs[0][:high]