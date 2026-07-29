class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1
        
        for i in range (len(s)//2 + 1):
            if s[l] != s[r]:
                return False 
            l +=1
            r -=1
        
        return True 
        
        
