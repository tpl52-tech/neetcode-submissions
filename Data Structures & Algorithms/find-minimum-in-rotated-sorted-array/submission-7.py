class Solution:
    def findMin(self, nums: List[int]) -> int:

        # draw shit out if test cases aren't passing. 

        l = 0
        m = 0 
        r = len(nums) - 1 
        m_value_min = nums[m]


        while l <= r: 
            m = l + (r - l) // 2
            m_value_min = min(nums[m], m_value_min)

            if nums[l] <= nums[r]:
                return m_value_min

            if nums[m] >= nums[l]: 
                l = m + 1
                m_value_min = min(m_value_min, nums[l])

            elif nums[m] <= nums[l]: 
                r = m - 1


