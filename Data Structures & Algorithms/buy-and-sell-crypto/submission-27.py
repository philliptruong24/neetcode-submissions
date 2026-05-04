class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        best_sold = 0

        for i in prices:
            if i < buy:
                buy = i
            best_sold = max(best_sold, i - buy)
        return best_sold
