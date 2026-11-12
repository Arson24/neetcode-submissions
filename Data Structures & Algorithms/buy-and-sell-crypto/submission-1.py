class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=float('inf')
        profit=0
        for price in prices:
            if price < mini:
                mini=price
            elif price-mini>profit:
                profit=price-mini
        return profit 