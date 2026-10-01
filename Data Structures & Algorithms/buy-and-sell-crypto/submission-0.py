class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j > i :
                    current_value = - prices[i] + prices[j]
                    if current_value > max:
                        max = current_value 
        if max <= 0:
            max = 0
        return max