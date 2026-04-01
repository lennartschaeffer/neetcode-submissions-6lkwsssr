class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #2,2,5
        #some if condition, if the current sum == target, append
        #for loop in nums

        res = []
        path = []

        def backtrack(start, path):
            if sum(path) > target:
                return
            if sum(path) == target:
                res.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])
                print(path)
                backtrack(i, path)
                path.pop()
            
        backtrack(0,[])

        return res