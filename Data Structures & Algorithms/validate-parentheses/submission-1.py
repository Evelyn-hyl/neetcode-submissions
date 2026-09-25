class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')' : '(', '}' : '{', ']' : '['}

        for char in s:
            if char in pairs:
                if not stack or (pairs.get(char) != stack[-1]):
                    return False
                
                stack.pop()
            else:
                stack.append(char)
        
        if stack:
            return False
        
        return True
        