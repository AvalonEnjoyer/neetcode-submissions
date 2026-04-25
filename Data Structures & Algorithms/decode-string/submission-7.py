class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)

        def decode(index: int, freq: int) -> int:
            temp =[]
            while index < n and s[index] != "]":
                if s[index].isdigit():
                    j = index
                    while s[j + 1].isdigit():
                        j += 1
                    # if multiplier has more than one char, take that as freq, skip to after "["
                    output, index = decode(j + 2, int(s[index:j + 1])) if index != j else decode(index + 2, int(s[index]))
                    temp += output
                else:
                    temp.append(s[index])
                index += 1
            return temp*freq, index
        return "".join(decode(0, 1)[0])