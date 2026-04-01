class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort the array, skip duplicates in my backtracking 
        # function. 
        res = []
        seen = []

        # 1,1,2
        # [1]
        # [], [1], 

        def backtrack(start, path):
            p = sorted(path[:].copy())
            if p not in seen:
                res.append(path[:])
                seen.append(p)

            for i in range(start, len(nums)):
                #skip dups
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])

        return res
