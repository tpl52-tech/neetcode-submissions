class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

       result = []
       i = 0 

       for i, a in enumerate(nums):
            if a > 0: 
                break 
            elif a == nums[i - 1] and i:
                continue

            l = i + 1 
            r = len(nums) - 1 
            
            while l < r: 
                curSum = nums[i] + nums[l] + nums[r]
                if curSum == 0: 
                    result.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1 
                    

                if curSum < 0:
                    l += 1
                if curSum > 0: 
                    r -= 1
                
        
            return result 


                    

        
