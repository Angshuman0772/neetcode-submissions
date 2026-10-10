class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: If lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Step 2: Count characters in s
        count_s = {}
        for ch in s:
            if ch in count_s:
                count_s[ch] += 1
            else:
                count_s[ch] = 1
        
        # Step 3: Count characters in t
        count_t = {}
        for ch in t:
            if ch in count_t:
                count_t[ch] += 1
            else:
                count_t[ch] = 1
        
        # Step 4: Compare the two dictionaries
        return count_s == count_t

