class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        lowest = prices[0]

        for price in prices:
            maxp = max(maxp, price-lowest)
            if price<lowest:
                lowest = price

        return maxp