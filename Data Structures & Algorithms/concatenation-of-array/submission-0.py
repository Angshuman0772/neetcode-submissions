class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ans.extend(nums + nums)
        return ans