class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 1
        for i in range (len(nums)):
            current = 1
            if nums[i] - 1 not in nums_set:
                next_elem = nums[i] + 1 
                while next_elem in nums_set:
                    current += 1 
                    next_elem += 1
                longest = max(longest, current)
        
        return longest 

                