class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characterSet = set()
        l = 0
        result = 0

        for r in range(len(s)):

            while s[r] in characterSet:
                characterSet.remove(s[l])
                l += 1
            characterSet.add(s[r])
            result = max(result, len(characterSet))
        return result