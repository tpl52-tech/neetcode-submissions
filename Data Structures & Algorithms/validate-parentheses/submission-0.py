class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        if stack == []:
            return True
        
        for char in s: 
            if char in closeToOpen: 
                if stack and stack[-1] == closeToOpen[char]: 
                    stack.pop()
                else:
                    return false 
            else: 
                stack.append(char)
        
        return stack != []

