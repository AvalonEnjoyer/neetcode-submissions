class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort()
        
        available, res = [], []
        t = tasks[0][0]
        i = 0
        n = len(tasks)

        while i<len(tasks) or available:
            while i<len(tasks) and t>=tasks[i][0]:
                    enqueue_time, process_time, idx = tasks[i]
                    heapq.heappush(available, (process_time, idx))
                    i+=1

            if not available:
                t = tasks[i][0]
            else:
                process_time, idx = heapq.heappop(available)
                t+=process_time
                res.append(idx)
        
        return res