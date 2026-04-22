class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
            similar backtracking template but now append based on a condition
            iterate through the numbers, keep track of curr
            at each step, check if sum(curr) == target
            our base case would be if sum > target
            at each step we backtrack on i, since we can re-use numbers 
        """

        res = []
        curr = []
        currSum = 0

        def backtrack(i):
            nonlocal currSum
            
            if currSum > target:
                return
            if currSum == target:
                res.append(curr.copy())
                return
            
            for j in range(i,len(nums)):
                curr.append(nums[j])
                currSum += nums[j]
                backtrack(j)
                top = curr.pop()
                currSum -= top
        
        backtrack(0)

        return res