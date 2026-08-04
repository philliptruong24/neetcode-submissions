class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        min_buy = prices[0]
        for i in prices:
            min_buy = min(i, min_buy)
            maxP = max(maxP, i - min_buy)
        return maxP

        



                