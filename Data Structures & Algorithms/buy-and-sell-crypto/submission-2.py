class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #keep track of the min buy and maxProfit
        #then for each element, if it is less than the min buy, update the min buy
        #otherwise, subtract the min buy from it and check if that is greater than the max profit
        minBuy = prices[0] if len(prices) > 0 else 0
        maxProfit = 0

        for i in range(1, len(prices)):
            if prices[i] < minBuy:
                minBuy = prices[i]
            else:
                profit = prices[i] - minBuy
                if profit > maxProfit:
                    maxProfit = profit
        
        return maxProfit