class Solution:
    from collections import Counter

    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if t is empty, no window needed
        if t == "":
            return ""

        # Count frequency of characters required in t
        countT = Counter(t)

        # Current sliding window character counts
        window = Counter()

        # have = how many characters currently satisfy required frequency
        # need = total unique characters we must satisfy
        have = 0 
        need = len(countT)

        # Store result indices and length
        res = [-1, -1]
        resLen = float("infinity")

        # Left pointer
        l = 0

        # Expand window using right pointer
        for r in range(len(s)):
            c = s[r]

            # Add current character to window
            window[c] += 1

            # Check if this character now satisfies required frequency
            if c in countT and window[c] == countT[c]:
                have += 1

            # When all required characters are satisfied
            while have == need:
                # Update result if this window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Try shrinking window from the left
                window[s[l]] -= 1

                # If removing this breaks requirement → reduce "have"
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                # Move left pointer forward
                l += 1

        # Extract result
        l, r = res

        # If no valid window found, return empty string
        return s[l:r+1] if resLen != float("infinity") else ""
            