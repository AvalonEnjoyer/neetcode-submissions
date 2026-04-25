class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n2 < n1:
            return False
        char_map = [0]*26
        for char in s1:
            char_map[ord(char)-ord("a")] += 1
        temp = [0]*26
        for right in range(n1, n2+1):
            left = right - n1
            if left == 0:
                for i in range(left, right):
                    temp[ord(s2[i]) - ord("a")] += 1
            else:
                temp[ord(s2[right-1]) - ord("a")] += 1
            if temp == char_map:
                return True
            temp[ord(s2[left]) - ord("a")] -= 1
        return False