class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0
        r = len(nums) - 1 
        result = []

        for i in range (len(nums)):
            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    result.append([l, i ,r])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < -nums[i]:
                    r -= 1
                elif nums[l] + nums[r] > -nums[i]:
                    l -= 1
                else: 
                    return result
