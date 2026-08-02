class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0 
        m = 0 
        r = len(nums) - 1 
        pivot = 0 

        while l < r: 
            m = l + (r - l) // 2 

            if nums[m] > nums[r]: 
                l = m + 1 
            elif nums[m] < nums[r]: 
                r = m 
        
        pivot = l
                
        part_1 = self.binarySearch(nums, target, 0, pivot - 1)
        part_2 = self.binarySearch(nums, target, pivot, len(nums) - 1)

        return max(part_1, part_2)
    
    def binarySearch(self, nums: List[int], target:int, l:int, r:int) -> int:
        
        while l <= r: 
            m = l + (r - l) // 2 

            if nums[m] == target: 
                return m
            elif nums[m] < target: 
                l = m + 1 
            elif nums[m] > target:
                r = m - 1 
            
        return -1 


            