class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if len(freq_map) == 0:
                freq_map[1] = [num]
            else:
                not_found = True
                for freq in freq_map.keys():
                    if num in freq_map[freq]:
                        freq_map[freq].remove(num)
                        freq_map[freq + 1] = freq_map.get(freq + 1, []) + [num]
                        not_found = False
                        break
                if not_found:
                    freq_map[1] += [num]
        frequencies = sorted(freq_map.keys(), reverse=True)

        frequent_elements = []
        i = 0
        while len(frequent_elements) < k:
            to_append = freq_map[frequencies[i]]
            for j,element in enumerate(to_append):
                frequent_elements.append(element)
                if j>=k:
                    break
            i = i+1

        return frequent_elements