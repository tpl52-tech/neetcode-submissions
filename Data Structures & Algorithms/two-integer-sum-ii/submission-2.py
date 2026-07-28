class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # why cant I just use the two-sum way? 
        # how am I going to incorporate 2 pointers into this? 

        # two-sum hash table to verify that the selected number from 
        # the left is indeed correct (has a corresponding right)
        # then, use the right pointer to go from the right to bring 
        # it down from the right, so you can easily return the 
        # [index1, index2] result in order 

        # oh fahh i cant do that since the solution must use O(1) additional
        # space 

        l = 0 
        r = len(numbers) - 1

        # I'm just going to try a time-inefficient solution

        while target - numbers[l] not in numbers: 
            l += 1
        # now we have the right smaller elem.
        while numbers[r] != target-numbers[l]:
            r -= 1

        return [l + 1, r + 1]

            
