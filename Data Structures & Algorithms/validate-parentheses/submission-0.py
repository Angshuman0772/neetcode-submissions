class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # mapping of closing brackets to opening brackets
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:   # it's a closing bracket
                # pop from stack if not empty, else assign dummy '#'
                top = stack.pop() if stack else '#'
                # check if it matches the correct opening bracket
                if mapping[char] != top:
                    return False
            else:  # it's an opening bracket
                stack.append(char)
        
        # string is valid only if no unmatched opening brackets remain
        return not stack