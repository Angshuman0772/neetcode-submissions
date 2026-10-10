class Solution:
    def trap(self, height: List[int]) -> int:
        width = len(height)
        area = 0

        for i in range(len(height)):
            leftMax = rightMax = height[i]

            for l in range(i):
                leftMax = max (leftMax, height[l])

            for r in range(i+1, len(height)):
                rightMax = max (rightMax, height[r])

            area += min(leftMax, rightMax) - height [i]
        return area
