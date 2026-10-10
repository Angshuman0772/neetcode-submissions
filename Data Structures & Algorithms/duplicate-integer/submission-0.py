class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Convert list to set. If length decreases, there are duplicates
        return len(nums) != len(set(nums))