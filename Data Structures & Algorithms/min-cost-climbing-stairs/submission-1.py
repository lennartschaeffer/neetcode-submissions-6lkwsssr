class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = [-1] * len(cost)
        def dfs(i):
            if i > len(cost)-1:
                return 0
            if self.memo[i] != -1:
                return self.memo[i]
            else:
                self.memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return self.memo[i]

        return min(dfs(0),dfs(1))



            