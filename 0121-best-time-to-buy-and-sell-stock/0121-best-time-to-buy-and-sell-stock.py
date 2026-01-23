class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        iterate thru the list of prices
        take element we're on and compare to the next one
        if the element we're on is greater then the next one for each element return 0
        if the next element is less then the previous one then we'll store it
        then do the subtraction & return profit
        """
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p

            profit = max(profit, p - buy_price)

        return profit


        