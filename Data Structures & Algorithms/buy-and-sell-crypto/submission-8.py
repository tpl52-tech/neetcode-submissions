class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        left = 0
        bestPrice = 0

        for right in range (len(prices)):

            bestPrice = max(bestPrice, prices[right] - prices[left])
            
            left = min(left, right)

        return bestPrice
