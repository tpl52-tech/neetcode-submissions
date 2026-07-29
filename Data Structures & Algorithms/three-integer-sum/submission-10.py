class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            if a == nums[i - 1]:
                continue

            l = i 
            r = len(nums) - 1
            
            while l < r: 
                curSum = nums[i] + nums[l] + nums[r]
                if curSum == 0: 
                    result.append([i, l, r])
                elif curSum < 0: 
                    l += 1
                elif curSum > 0:
                    r -= 1
        
        return result 

        
