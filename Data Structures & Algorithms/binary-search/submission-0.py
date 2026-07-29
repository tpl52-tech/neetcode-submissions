class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        m = 0 
        r = len(nums) - 1

        while l < r: 
            m = m + int((r - l) / 2)
            
            if nums[m] > target:
                l = m 
            elif nums[m] < target:
                r = m 
            else: 
                return m 
        
        return -1