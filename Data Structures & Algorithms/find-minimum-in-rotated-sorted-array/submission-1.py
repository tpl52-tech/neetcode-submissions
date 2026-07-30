class Solution:
    def findMin(self, nums: List[int]) -> int:

        # draw shit out if test cases aren't passing. 

        l = 0
        m = 0
        r = len(nums) - 1
        
        while l <= r: 

            if nums[l] <= nums[r]: 
                return nums[l]
            
            m = l + (r - l) // 2

            if nums[m] >= nums[l]: 
                l = m + 1 
            elif nums[l] > nums[m]: 
                r = m
        
        return -1
        