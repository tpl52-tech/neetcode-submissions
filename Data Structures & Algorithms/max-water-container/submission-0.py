class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # you have to find the maximum length / height combo between any of 
        # the two bars.
        # the minimum of the heights will determine the height of the container. 
        # the distance between the two indices is the width

        l = 0 
        r = len(heights) - 1 
        maxLength = min(heights[l], heights[r]) * (r - l)


        while l < r: 

            current = min(heights[l], heights[r]) * (r - l)
            maxLength = max(current, maxLength)

            if heights[l] >= heights[r]: 
                r -= 1 
            elif heights[l] < heights[r]:
                l += 1  

        return maxLength
            


