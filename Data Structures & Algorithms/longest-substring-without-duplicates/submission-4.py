from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = Counter() # character -> freq
        l = 0
        result = 0

        for r, char in enumerate(s):
            count[char] += 1

            while count[char] > 1:
                count[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)

        return result
            