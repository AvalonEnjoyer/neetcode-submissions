class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = {i:[] for i in range(numCourses)}

        for crs,preq in prerequisites:
            mapping[crs].append(preq)
        visiting = set()
        def dfs(c):
            if c in visiting:
                return False
            if mapping[c]==[]:
                return True
            visiting.add(c)
            for pre in mapping[c]:
                if not dfs(pre):
                    return False
            visiting.remove(c)
            mapping[c]=[]
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True