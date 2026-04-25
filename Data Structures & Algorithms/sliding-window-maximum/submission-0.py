class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        import collections
        q = collections.deque() # indices stored in the deque
        l = r = 0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove Left value from the window if it's out of bounds
            if l > q[0]:
                q.popleft()

            # if the window size is right
            if (r-l+1) == k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output