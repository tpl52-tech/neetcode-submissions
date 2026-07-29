class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        left = 0
        bestPrice = 0

        for right in range (len(prices)):

            bestPrice = max(bestPrice, prices[right] - prices[left])
            
            if prices[left] < prices[right]: 
                left +=1

        return bestPrice
