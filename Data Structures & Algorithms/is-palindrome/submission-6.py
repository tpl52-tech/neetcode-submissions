class Solution:
    def isPalindrome(self, s: str) -> bool:

        s1 = ""

        for char in s: 
            if char.isalpha(): 
                s1 += char
        
        s1 = s1.upper()

        # finding what it is, reversed: 

        r = ""

        for i in range(len(s1) -1, 0, -1): 
            r += s1[i]
        
        return r == s1
        
