class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                prof = prices[j] - prices[i]
                if prof > 0:
                    profits.append(prof)
        
        if(len(profits) > 0):
            return max(profits)
        else:
            return 0