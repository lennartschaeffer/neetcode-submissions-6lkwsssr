class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # use backtracking, have a recursive dfs function
        # that has a start parameter and a current path
        # explores the from start to end of array and appends
        # each path to the result
        res = []
        path = []
        
        def backtrack(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])

        return res