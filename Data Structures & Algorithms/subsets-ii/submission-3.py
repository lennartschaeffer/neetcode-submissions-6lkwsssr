class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
            similar to combination sum II in the sense that we can have duplicates
            but have to check that we're not going into a duplicate branch from 
            the same lvl. 
                the problem with that though is that we can't sort. 
                maybe we can instead keep track of indices we've seen in the recursion

        """

        res = []
        curr = []
        nums.sort()

        def backtrack(i):
            res.append(curr.copy())

            for j in range(i,len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                curr.append(nums[j])
                backtrack(j+1)
                curr.pop()
        
        backtrack(0)

        return res

