class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_list = sorted(set(nums))
        if not nums:
            return 0
        
        max_len = 1
        current_len = 1
        for i in range(len(sorted_list) - 1):
            if sorted_list[i+1] == sorted_list[i] + 1:
                current_len += 1
            else:
                max_len = max(max_len, current_len)
                current_len = 1
        
        return max(max_len, current_len)