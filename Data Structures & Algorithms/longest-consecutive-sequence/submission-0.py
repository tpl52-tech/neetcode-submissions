class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # plan: make a hash map. key = each number + 1 value = the number
        # then, check consecutively if it's in there. see the longest
        # sequence u can make, and return 

        intToNext = {}

        for i in range (len(nums)):
            intToNext[nums[i] + 1] = nums[i]
        
        longest = 0

        for i in range (len(nums)): 
            pointer = nums[i]
            while pointer in intToNext: 
                longest += 1
                pointer +=1
        
        return longest
                

