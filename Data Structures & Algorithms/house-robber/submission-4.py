class Solution:
    def rob(self, nums: List[int]) -> int:
        # [1,1,3,3]
        # amt = max(1 + 3 )
        self.memo = {}

        def dfs(i):
            if i >= len(nums):
                return 0

            if i in self.memo:
                return self.memo[i]
            else:
                self.memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))

            return self.memo[i]

        return dfs(0)