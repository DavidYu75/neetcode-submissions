class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of lowest stock price
        # iterate through the prices
        # i = 0
        # lowest = 10
        # i = 1
        # current_price = 1
        # lowest = 10
        # profit = 1 - 10 = -9
        # lowest = min(current, lowest) = 1
        # i = 2
        # lowest = 1
        # current_price = 5
        # profit = 5 - 1 = 4

        lowest = prices[0]
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price - lowest)
            lowest = min(lowest, price)
        
        return max_profit