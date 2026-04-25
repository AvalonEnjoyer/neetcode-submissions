class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        def decode(index: int) -> int:
            temp = []
            num = 0
            while index < n:
                if s[index].isdigit():
                    num = num*10 + int(s[index])
                elif s[index]=="[":
                    output, index = decode(index + 1)
                    temp.extend(output*num)
                    num=0
                elif s[index]=="]":
                    return temp, index
                else:
                    temp.append(s[index])
                index += 1
            return temp, index

        return "".join(decode(0)[0])