class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available, pending = [],[]
        for i, task in enumerate(tasks):
            task.append(i)
            heapq.heappush(pending, task)

        t=0
        res = []

        while available or pending:
            while pending and t>= pending[0][0]:
                enqueue_time, process_time, i = heapq.heappop(pending)
                heapq.heappush(available, (process_time,i))
            if not available:
                enqueue_time, process_time, i = heapq.heappop(pending)
                t = enqueue_time
            else:
                process_time, i = heapq.heappop(available)

            t+=process_time
            res.append(i)
        
        return res