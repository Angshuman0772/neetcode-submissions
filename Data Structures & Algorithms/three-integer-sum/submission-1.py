class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: sort the array

        for i, n in enumerate(nums):
            # Skip duplicate values for the first number
            if i > 0 and n == nums[i - 1]:
                continue

            l = i + 1              # left pointer
            r = len(nums) - 1     # right pointer

            while l < r:
                threeSum = n + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1        # need a bigger sum → move left pointer right
                elif threeSum > 0:
                    r -= 1        # need a smaller sum → move right pointer left
                else:
                    res.append([n, nums[l], nums[r]])  # found valid triplet

                    l += 1
                    # Skip duplicates for the second number
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res