class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0

        for i in prices:
            buy = min(buy, i)
            max_profit = max(max_profit, i - buy)
        
        return max_profit
