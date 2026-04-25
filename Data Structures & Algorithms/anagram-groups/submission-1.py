class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = []
        char_maps = {}
        for string in strs:
            ordered_string = "".join(sorted(string))
            if ordered_string not in char_maps:
                char_maps.setdefault(ordered_string, [string])
            else:
                char_maps[ordered_string] += [string]
        for keys, values in char_maps.items():
            sublists.append(values)
        return sublists