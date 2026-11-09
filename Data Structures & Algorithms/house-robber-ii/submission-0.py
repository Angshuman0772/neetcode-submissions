class Solution:
    def helper(self, nums):
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n # index 0 contains house 1
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            take = dp[i - 2] + nums[i]
            skip = dp[i - 1]
            dp[i] = max(take, skip)
        return dp[-1]


    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(
            self.helper(nums[1:]),
            self.helper(nums[:-1])
        )