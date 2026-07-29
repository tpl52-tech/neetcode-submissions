class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        left = 0
        bestPrice = 0

        for right in range (len(prices)):

            while prices[right] - prices[left] > bestPrice: 
                bestPrice = max(bestPrice, prices[right] - prices[left])
                left += 1

        return bestPrice
