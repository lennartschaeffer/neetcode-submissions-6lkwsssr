class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            maxSoFar = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxSoFar = max(maxSoFar, dp[j])
            dp[i] += maxSoFar
        
        return max(dp)