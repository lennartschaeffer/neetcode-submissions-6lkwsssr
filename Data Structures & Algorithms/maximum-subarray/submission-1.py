class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # a brute force appraoch could be to run a doulbe
        # for loop, and find the sum from i to j

        maxSum = nums[0]

        for i in range(len(nums)):
            curr = 0
            for j in range(i,len(nums)):
                curr += nums[j]
                maxSum = max(maxSum,curr)

        return maxSum