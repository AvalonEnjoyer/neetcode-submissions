class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n=len(s)
        def decode(index: int, freq:int) -> int:
            start = index
            for _ in range(freq):
                index = start
                while index<n and s[index]!="]":
                    if s[index].isdigit():
                        j = index
                        while s[j + 1].isdigit():
                            j += 1
                        index = decode(j + 2, int(s[index:j+1])) if index != j else decode(index + 2, int(s[index]))
                    else:
                        stack.append(s[index])
                    index+=1
            return index
        decode(0,1)
        return "".join(stack)