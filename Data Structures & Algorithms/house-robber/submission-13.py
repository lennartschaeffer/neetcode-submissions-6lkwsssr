class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
                
            rob = nums[i] + dfs(i+2)
            dontRob = dfs(i+1)

            memo[i] = max(rob,dontRob)

            return memo[i]
        
        return dfs(0)
