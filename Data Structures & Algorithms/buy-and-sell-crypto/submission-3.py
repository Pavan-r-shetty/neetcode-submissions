class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        lowest = prices[0]  # Track minimum price seen so far
        
        for price in prices:
            # Can we sell at current price for better profit?
            maxp = max(maxp, price - lowest)
            # Update the minimum price if needed
            if price < lowest:
                lowest = price
                
        return maxp

