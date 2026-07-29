class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # strat: make a list of all of the times with different 
        # bananas-per-hour eating rates, from 1 to 
        # the height of the highest pile. Perform 
        # binary search on it, each time calculating the number 
        # of hours it would take to eat the banaanas 
        l = 1
        m = 1 
        r = max(piles)
        min_so_far = r

        while l <= r: 
            m = l + (r - l) // 2
            
            # calculate the time 
            time = 0
            for i in range(len(piles)): 
                time += math.ceil(piles[i] / m)
            
            if time <= h:
                r = m - 1
                min_so_far = min(m, min_so_far)
            else:
                l = m + 1             
        
        return min_so_far
        



