class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        result = 0
        while l < r:
            area = (r - l) * min (heights[l], heights[r]) # (r-l) forms the length and height is the width
            result = max(result, area)
            if heights[l] <= heights[r]:
                l += 1
            else: # condition heights[r] <= heights[l]:
                r -= 1
        return result
