class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 2 * sum(set(nums)) - sum(nums)
        return single