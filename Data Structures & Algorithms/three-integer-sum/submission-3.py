class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                currSum = n + nums[l] + nums[r]
                if currSum > 0:
                    r -= 1
                elif currSum < 0:
                    l += 1
                else:
                    list = [n, nums[l], nums[r]]
                    res.append(list)
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return res
                
