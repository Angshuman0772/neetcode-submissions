# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         ch_to_count = {} # ch -> count
#         result = 0
#         l = 0
#         maxCount = 0

#         for r in range(len(s)):
#             ch_to_count[s[r]] = 1 + ch_to_count.get(s[r], 0)
#             maxCount = max(maxCount, ch_to_count[s[r]])

#             while (r - l + 1) - maxCount > k:
#                 ch_to_count[s[l]] -= 1
#                 l += 1
#             result = max(result, r - l + 1)
#         return result

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = Counter()
        result = 0
        l = 0
        maxCount = 0

        for r in range(len(s)):
            count[s[r]] += 1

            maxCount = max(maxCount, count[s[r]])

            # # Shrink the window from the left until it becomes valid again
            while (r - l + 1) - maxCount > k:
                count[s[l]] -= 1
                l += 1
        
            result = max(result, r - l + 1)
        return result