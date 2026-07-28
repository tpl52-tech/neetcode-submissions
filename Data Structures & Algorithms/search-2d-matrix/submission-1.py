class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # strategy: do binary search on the middle row. check 
        # if leftmost integer < target < rightmost integer. 
        # do this for each row found w search, comparing with target. 
        # then do binary search on the row once you know 
        # for sure that that row is the only one that can contain target

        l_matrixi = 0
        m_matrixi = 0
        r_matrixi = len(matrix) - 1

        # find the list it has to be in 

        while l_matrixi <= r_matrixi : 
            m_matrixi = l_matrixi + (r_matrixi - l_matrixi) // 2
            
            if matrix[m_matrixi][0] > target: # if the leftmost integer is to the right of (bigger than) target
                r_matrixi = m_matrixi - 1
            elif matrix[m_matrixi][-1] < target: 
                l_matrixi = m_matrixi + 1
            else: 
                break

        # binary search on the list that must contain target

        l = 0 
        m = 0
        r = len(matrix[m_matrixi]) - 1
        m_matrix = matrix[m_matrixi]

        while l <= r: 
            m = l + (r - l) // 2

            if m_matrix[m] > target: 
                r = m - 1 
            elif m_matrix[m] < target: 
                l = m + 1 
            else: 
                return True
        

        return False 