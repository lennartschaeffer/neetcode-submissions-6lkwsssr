class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
            in this case we'd want to just iterate from 0, not from i to len(nums)
            and then maybe skip if nums[i] == nums[j]
        """

        res = []
        curr = []
        seen = set()

        def backtrack(i):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for j in range(len(nums)):
                if nums[j] in seen:
                    continue
                curr.append(nums[j])
                seen.add(nums[j])
                backtrack(j+1)
                rem = curr.pop()
                seen.remove(rem)
            
        
        backtrack(0)
        
        return res