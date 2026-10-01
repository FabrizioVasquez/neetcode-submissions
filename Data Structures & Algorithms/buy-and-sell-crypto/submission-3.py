class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_value = 99999
        max_profit = 0
        for i in range(len(prices)-1):
            if prices[i] < min_price_value:
                min_price_value = prices[i]
            
            profit =  prices[i+1] - min_price_value

            if profit > max_profit:
                max_profit = profit
        return max_profit