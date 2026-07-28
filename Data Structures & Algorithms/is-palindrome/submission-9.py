class Solution:
    def isPalindrome(self, s: str) -> bool:

        s1 = "".join(char for char in s if char.isalpha() or char.isnumeric())
        
        s1 = s1.upper()

        # finding what it is, reversed: 

        r = ""

        for i in range(len(s1) -1, -1, -1): 
            r += s1[i]
        
        return r == s1
        
