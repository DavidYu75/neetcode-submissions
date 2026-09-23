class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # min_buy = prices[0]

        # for sell in prices:
        #     max_profit = max(max_profit, sell - min_buy)
        #     min_buy = min(min_buy, sell)
        
        # return max_profit

        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
            right += 1

        return max_profit