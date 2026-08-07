class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort()

        pending = tasks
        available, res = [], []

        t = pending[0][0]
        i = 0
        n = len(pending)
        while i<len(pending) or available:
            while i<len(pending):
                if pending[i][0] <= t:
                    enqueue_time, process_time, idx = pending[i]
                    heapq.heappush(available, (process_time, idx))
                    i+=1
                else:
                    break
            if not available:
                t = pending[i][0]
            else:
                process_time, idx = heapq.heappop(available)
                t+=process_time
                res.append(idx)
        
        return res