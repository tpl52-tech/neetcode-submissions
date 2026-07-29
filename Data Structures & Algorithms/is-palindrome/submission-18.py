class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1
        
        while (l < r):
            if not s[l].isalnum():
                continue
            if not s[r].isalnum():
                continue
            if s[l] != s[r]:
                return False           
            l +=1
            r -=1

        return True 
        
        
