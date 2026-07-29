class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}
        
        for char in s: 
            if char in closeToOpen: 
                if stack and stack[-1] == closeToOpen[char]: 
                    stack.pop()
                else:
                    return false 
            else: 
                stack.append(char)
        
        if stack == []:
            return True
        
        return stack != []

