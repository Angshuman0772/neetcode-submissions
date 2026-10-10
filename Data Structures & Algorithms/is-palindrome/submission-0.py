class Solution:
    def isPalindrome(self, s: str) -> bool:
         # keep only alphanumeric chars and lowercase them
        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
        
        # check palindrome
        return cleaned == cleaned[::-1]