from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()      # character -> frequency in current window
        result = 0             # length of longest valid window found so far
        l = 0                  # left pointer of sliding window
        maxCount = 0           # highest frequency of any character seen in the current window

        """ 
        We can also use enumerate as so

        for r, ch in enumerate(s):
            count[ch] += 1
            maxCount = max(maxCount, count[ch])

            while (r - l + 1) - maxCount > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)
        """

        for r in range(len(s)):
            count[s[r]] += 1   # expand window by including s[r]

            # update the highest frequency character count in the window
            maxCount = max(maxCount, count[s[r]])

            # if replacements needed > k, shrink window from the left
            while (r - l + 1) - maxCount > k:
                count[s[l]] -= 1
                l += 1

            # update longest valid window length
            result = max(result, r - l + 1)

        return result