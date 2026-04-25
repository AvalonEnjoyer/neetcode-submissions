class Solution:
    # Solution 3 - 100% runtime and 95.35% memory
    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        for string in strs:
            encoded_str.append(str(len(string))+"#"+string)
        return "".join(encoded_str)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j=i
            while s[j] != "#":
                j += 1
            word_length = int(s[i:j])
            strs.append(s[j+1:j+1+word_length])
            i = j+word_length+1
        return strs