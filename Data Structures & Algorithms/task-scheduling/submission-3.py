class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        char_map = Counter(tasks)
        char_map = [cnt for cnt in char_map.values()]
        heapq.heapify_max(char_map)
        q = deque()
        time = 0 
        
        while q or char_map:
            time += 1
            print(time)
            if not char_map:
                time = q[0][1]
            else:
                task = heapq.heappop_max(char_map) -1
                if task:
                    q.append([task, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush_max(char_map, q.popleft()[0])
        return time
            
        # When do we have more than 1 cycle?
        # Max heap with all the tasks