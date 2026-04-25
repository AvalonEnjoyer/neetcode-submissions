class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = []
        char_maps = {}
        for i, string in enumerate(strs):
            ordered_string = "".join(sorted(string))
            if ordered_string not in char_maps:
                char_maps.setdefault(ordered_string, [i])
            else:
                char_maps[ordered_string] += [i]
        for key in char_maps.keys():
            sublist = []
            for value in char_maps[key]:
                sublist.append(strs[value])
            sublists.append(sublist)
        return sublists