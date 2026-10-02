class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adj = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            adj[src].append(dst)
            indegree[dst]+=1
        
        q = [i for i,n in enumerate(indegree) if n==0]
        q = deque(q)
        finish = 0

        while q:
            node = q.popleft()
            finish+=1
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        
        return finish == numCourses
