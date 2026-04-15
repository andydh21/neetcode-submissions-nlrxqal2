class Solution:
    def isValid(self, s: str) -> bool:
        # Quick check for odd lengths
        if len(s) % 2 != 0:
            return False
            
        stack = []
        # A dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Get the top element of the stack if it exists, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the popped element doesn't match the required opening bracket, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty at the end, all brackets were matched correctly
        return not stack
        