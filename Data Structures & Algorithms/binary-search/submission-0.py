class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2  # middle index
            
            if nums[mid] == target:
                return mid  # target found
            elif nums[mid] < target:
                left = mid + 1  # search in right half
            else:
                right = mid - 1  # search in left half
        
        return -1  # target not found