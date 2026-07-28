class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        charToIndex = {}
        longest = 0

        for right in range (len(s)):

            if s[right] in charToIndex:
                left = max(left, charToIndex[s[right]]+1)
            
            longest = max(longest, right - left + 1)
            charToIndex[s[right]] = right

        return longest 
