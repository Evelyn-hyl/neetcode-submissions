class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        window_start = 0
        window_end = 1

        for window_end in range(len(prices)):
            if prices[window_start] > prices[window_end]:
                window_start = window_end
            else:
                max_profit = max(max_profit, (prices[window_end] - prices[window_start]))
        
        return max_profit