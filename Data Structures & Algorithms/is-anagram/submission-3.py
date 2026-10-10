class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Step 2: Sort both strings
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        
        # Step 3: Compare sorted strings
        return sorted_s == sorted_t
