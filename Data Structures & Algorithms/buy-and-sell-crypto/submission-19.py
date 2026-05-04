class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = prices[0]
        best_sold = 0

        for i in prices[1:]:
            if i < buy:
                buy = sell = i
            elif sell < i:
                sell = i
            if sell - buy > best_sold:
                best_sold = sell - buy
        return best_sold
