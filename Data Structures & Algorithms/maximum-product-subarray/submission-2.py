class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxSoFar = 1
        minSoFar = 1

        for n in nums:
            tmp = maxSoFar * n
            maxSoFar = max(tmp, n * minSoFar, n)
            minSoFar = min(tmp, n * minSoFar, n)
            res = max(res,maxSoFar)

        return res


        