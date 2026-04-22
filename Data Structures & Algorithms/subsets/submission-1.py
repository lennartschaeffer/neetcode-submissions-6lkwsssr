class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
            use backtracking 
                run a recursive function and iterate through elements
                keep track of current subset 
                don't necessarily need a base case to append to result array,
                we want to append at every call in the recursion
                at each step append an element, then call function recursively
                after the recursive call we would pop

            [1,2,3]
            
        """

        res = []
        curr = []

        def backtrack(i):
            res.append(curr.copy())

            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(j+1)
                curr.pop()
        
        backtrack(0)

        return res
