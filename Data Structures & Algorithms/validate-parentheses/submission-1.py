class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ')': '(', 
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in hashmap: # if it's a closing bracket
                if stack and stack[-1] == hashmap[ch]:
                    stack.pop() # remove the opening bracket
                else:
                    return False
            else: 
                stack.append(ch) # push opening bracket onto the stack
        return True if not stack else False # if stack is empty, all brackets matched correctly