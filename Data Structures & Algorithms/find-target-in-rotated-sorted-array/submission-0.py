class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # strategy: find the side that has the crack in it. you 
        # can then make the array into 2 sorted array. then, do binary search on each side
        # thats O(log n)

        break_index = self.find_break_index(nums, target)
        sub_list_1 = nums[0 : break_index]
        sub_list_2 = nums[break_index : len(nums)]

        result = max(self.binarySearch(sub_list_1, target), self.binarySearch(sub_list_2, target))
        return result 

        
    def find_break_index(self, nums: List[int], target: int) -> int:

        l = 0 
        m = 0 
        r = len(nums) - 1
        safe = nums[m]

        while l <= r: 
            m = l + (r - l) // 2 

            safe = min(nums[m], safe)

            if nums[l] <= nums[r]:
                return min(safe, nums[l])
            
            if nums[m] >= nums[l]:
                l = m + 1 
                safe = min(safe, nums[l])
            elif nums[m] <= nums[r]:
                r = m - 1 

    def binarySearch (self, nums: List[int], target: int): 
        l = 0 
        m = 0 
        r = len(nums) - 1 
        
        while l <= r: 
            m = l + (r - l) // 2

            if nums[m] > target: 
                r = m - 1 
            elif nums[m] < target: 
                l = m + 1 
            else: 
                return m 
        
        return - 1 
        
            