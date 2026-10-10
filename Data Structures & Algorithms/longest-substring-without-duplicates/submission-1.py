#  "zxyzxyz"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:      
        maxLength = 0

        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                else:
                    charSet.add(s[j])
            maxLength = max(maxLength, len(charSet))
        return maxLength