class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        included = False
        char_map = [0]*26
        for char in s1:
            char_map[ord(char)-ord("a")] += 1
        n1 = len(s1)
        n2 = len(s2)
        if n2<n1:
            return included
        right = n1
        left = 0
        while right <= n2:
            temp = {}
            for left in range(left, right):
                key = ord(s2[left]) - ord("a")
                temp[key] = temp.get(key,0) + 1
            for key, value in temp.items():
                if char_map[key] == value:
                    included = True
                else:
                    included = False
                    break
            if included:
                break
            right += 1
            left = right - n1
        return included 