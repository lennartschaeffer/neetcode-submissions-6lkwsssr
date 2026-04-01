class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        # at each step, we have to make the choice, choose the coin or dont
        self.memo = {}
        def dfs(i, currAmount):
            if(i,currAmount) in self.memo:
                return self.memo[(i,currAmount)]
            if i > len(coins)-1 or currAmount < 0:
                return float("inf")
            if currAmount == 0:
                return 0
            
            #result is the minimum number of steps it take
            res = min(1 + dfs(i, currAmount - coins[i]), dfs(i+1, currAmount))
            self.memo[(i,currAmount)] = res
            return res
        
        res = dfs(0,amount)

        return res if res < float("inf") else -1
            