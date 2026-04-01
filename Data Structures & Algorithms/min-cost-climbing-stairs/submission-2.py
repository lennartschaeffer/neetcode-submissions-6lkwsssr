class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # 1,4,4,4,5,0
        # 
        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0],cost[1])
        
        # self.memo = [-1] * len(cost)
        # def dfs(i):
        #     if i > len(cost)-1:
        #         return 0
        #     if self.memo[i] != -1:
        #         return self.memo[i]
        #     else:
        #         self.memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

        #     return self.memo[i]

        # return min(dfs(0),dfs(1))



            