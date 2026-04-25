class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights) # there will need to be at least one ship to carry the weight of the biggest element
        r = l*len(weights)
        # if it does not decrease the number of days, keep checking lower
        def check_days(capacity):
            days_needed = 1
            current = 0
            for w in weights:
                if current + w > capacity:
                    days_needed += 1
                    current = w
                else:
                    current += w
            return days_needed


        while l<=r:
            mid = (l+r)//2
            curr_days = check_days(mid)
            if curr_days<=days:
                r = mid-1
            else:
                l = mid+1
        return r if curr_days==0 else r+1