class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = collections.deque() # index
        l = r = 0

        while r < len(nums):
            # remove smaller element from queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # left value goes out of window
            if l > q[0]:
                q.popleft()
            # check that window is at least size k
            if (r + 1) >= k:
                result.append(nums[q[0]])
                l += 1
            r += 1
        return result