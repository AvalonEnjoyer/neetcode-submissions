class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights) # there will need to be at least one ship to carry the weight of the biggest element
        r = l*len(weights)
        # if it does not decrease the number of days, keep checking lower
        def check_days(capacity):
            res = 0
            running_sum = 0
            for w in weights:
                if running_sum + w < capacity:
                    running_sum += w
                else:
                    if running_sum + w == capacity:
                        running_sum = 0
                    else:
                        running_sum = w
                    res+=1
            return res+1 if running_sum != 0 else res
        candidate = 0
        while l<=r:
            mid = (l+r)//2
            curr_days = check_days(mid)
            print(mid, curr_days)
            if curr_days<=days:
                if curr_days == days:
                    candidate = mid
                r = mid-1
            else:
                l = mid+1
        print(f"Candidate:{candidate} r:{r}")
        return r+1 if candidate==0 else candidate