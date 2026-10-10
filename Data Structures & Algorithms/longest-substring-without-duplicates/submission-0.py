#  "zxyzxyz"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:      
        maxLength = 0

        for i, num1 in enumerate(s):
            charSet = set()
            for j, num2 in enumerate(s[i:]):
                if num2 in charSet:
                    break
                else:
                    charSet.add(num2)
            maxLength = max(maxLength, len(charSet))
        return maxLength

