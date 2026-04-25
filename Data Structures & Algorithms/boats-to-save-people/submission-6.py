class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if people is None:
            return
        people.sort()
        print(people)
        res = 0
        n = len(people)
        i = 0
        j = n-1
        temp = 0
        while i <= j:
            if people[j] == limit:
                res += 1
                j -= 1
            else:
                if i == j:
                    res+=1
                    break
                temp = people[i] + people[j]
                if temp == limit:
                    res += 1
                    i+=1
                    j-=1
                elif temp > limit:
                    res += 1
                    j-=1
                else:
                    new_temp = people[i]+people[i+1]
                    if new_temp<limit:
                        i+=2
                    else:
                        i+=1
                        j-=1
                    res += 1
        return res