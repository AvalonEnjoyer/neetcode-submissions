class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        q = deque([0])
        seen = [False]*(amount+1)
        seen[0] = True
        steps = 0
        
        while q:
            steps+=1
            for _ in range(len(q)):
                existing = q.popleft()
                for coin in coins:
                    summa = coin+existing
                    if summa == amount:
                        return steps
                    elif summa > amount or seen[summa]:
                        continue
                    seen[summa] = True
                    q.append(summa)

        return -1