class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indices = list(range(n))
        indices.sort(key = lambda i: (tasks[i][0],i))
        
        class Task():
            def __init__(self, idx):
                self.idx = idx
            
            def __lt__(self, other):
                if tasks[self.idx][1] != tasks[other.idx][1]:
                    return tasks[self.idx][1] < tasks[other.idx][1]
                return self.idx < other.idx

        t=i=0
        min_heap, res = [], []
        
        while min_heap or i<n:
            while i<n and t>=tasks[indices[i]][0]:
                heapq.heappush(min_heap, Task(indices[i]))
                i+=1

            if not min_heap:
                t = tasks[indices[i]][0]
            else:
                task = heapq.heappop(min_heap)
                t+=tasks[task.idx][1]
                res.append(task.idx)
        
        return res