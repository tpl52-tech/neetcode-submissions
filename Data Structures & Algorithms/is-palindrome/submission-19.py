class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1

        s1 = s.upper()
        
        while (l < r):
            if not s1[l].isalnum():
                continue
            if not s1[r].isalnum():
                continue
            if s1[l] != s1[r]:
                return False           
            l +=1
            r -=1

        return True 
        
        
