class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        for i, a in enumerate(nums): # 0, 0, 0
            if i and a == nums[i - 1]:
                continue

            if a > 0:
                break
            
            l = i + 1
            r = len(nums) - 1
            
            while l < r: 
                curSum = nums[i] + nums[l] + nums[r]
                if curSum == 0: 
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1 
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif curSum < 0: 
                    l += 1
                elif curSum > 0:
                    r -= 1
        
        return result 

        
