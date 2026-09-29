class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        status = {}
        for trustee in trust:
            if trustee[0] not in status:
                status[trustee[0]]=[]
            status[trustee[0]].append(trustee[1])
        
        candidates = status[trustee[0]]

        def candidate_check(candidate):
            for trusted in status.values():
                if candidate not in trusted:
                    return -1
                if candidate in status:
                    return -1
            return candidate

        for candidate in candidates:
            if candidate_check(candidate) == candidate:
                return candidate
        return -1