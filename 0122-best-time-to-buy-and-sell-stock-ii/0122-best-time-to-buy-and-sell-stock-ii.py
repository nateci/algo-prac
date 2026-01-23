class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        each day decide to buy/sell stock
        can only hold one at a time
        but can sell and buy the stock multiple times same day
        find max profit
        """


        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                profit = prices[i] - prices[i-1]
                max_profit += profit

        return max_profit





        