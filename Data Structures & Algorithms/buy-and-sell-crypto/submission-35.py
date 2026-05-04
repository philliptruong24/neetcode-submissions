class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_buy = prices[0]
        # max_profit = 0

        # for i in prices:
        #     min_buy = min(min_buy, i)
        #     max_profit = max(max_profit, i - min_buy)
        
        # return max_profit

        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                curr_profit = prices[r] - prices[l]
                max_profit = max(max_profit, curr_profit)
            else:
                l = r
            r += 1
        return max_profit

                