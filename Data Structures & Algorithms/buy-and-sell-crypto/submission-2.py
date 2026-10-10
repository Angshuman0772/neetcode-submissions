class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float('inf')

        for p in prices:
            if p < minPrice:
                minPrice = p
            currProfit = p - minPrice
            if currProfit > maxProfit:
                maxProfit = currProfit
        return maxProfit