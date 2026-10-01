class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        mapping = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            mapping[crs].append(pre)

        print(mapping)

        visited = set()

        def dfs(crs):
            if crs in visited:
                # cycle detected
                return False
            if mapping[crs]==[]:
                return True
            visited.add(crs)
            for pre in mapping[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            mapping[crs]=[]
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
        