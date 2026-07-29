class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    

        left = 0
        bestPrice = 0

        for right in range (len(prices)):
            
            if prices[right] - prices[left] > bestPrice: 
                left +=1
                bestPrice = max(bestPrice, prices[right] - prices[left])

        return bestPrice
