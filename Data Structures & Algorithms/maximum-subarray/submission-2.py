class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # a brute force appraoch could be to run a doulbe
        # for loop, and find the sum from i to j
        #[2,-3,4,-2,2,1,-1,4]
        # 8
        maxSum = max(nums)
        curr = 0
        for n in nums:
            if curr < 0:
                curr = 0
            curr += n
            maxSum = max(maxSum,curr)

        return maxSum

        