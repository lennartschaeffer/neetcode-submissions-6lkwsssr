class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
            [2,-1,1,2]
            [2,1,2,4]
            keep track of a prefix array and at each step check
            have we seen currSum - k before? if so how many times
                this tells us: can we chop off some subarray of the current 
                sub array to give us k?
        """

        seen = {0:1}
        curr = 0
        res = 0

        for n in nums:
            curr += n
            rem = curr - k
            res += seen.get(rem,0)
            seen[curr] = seen.get(curr, 0) + 1
        
        return res
            