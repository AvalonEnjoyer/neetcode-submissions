class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        included = False
        char_map = [0]*26
        for char in s1:
            char_map[ord(char)-ord("a")] += 1
            del char
        n1 = len(s1)
        n2 = len(s2)
        if n2 < n1:
            return False
        temp = {}
        for right in range(n1, n2+1):
            left = right - n1
            if left == 0:
                for i in range(left, right):
                    key = ord(s2[i]) - ord("a")
                    temp[key] = temp.get(key,0) + 1
            else:
                key = ord(s2[right-1]) - ord("a")
                temp[key] = temp.get(key, 0) + 1
            for key, value in temp.items():
                if char_map[key] == value:
                    included = True
                else:
                    included = False
                    break
            if included:
                return True
            if temp[ord(s2[left]) - ord("a")] != 0:
                temp[ord(s2[left]) - ord("a")] -= 1
            else:
                del temp[ord(s2[left]) - ord("a")]
        return included