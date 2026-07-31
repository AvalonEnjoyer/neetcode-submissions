class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        maxf = max(count)
        max_count = 0
        for i in count:
            max_count += 1 if i == maxf else 0 
        print(maxf, max_count)
        time = (maxf-1)*(n+1)+max_count
        return max(len(tasks), time)