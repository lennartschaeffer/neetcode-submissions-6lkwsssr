class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # start from n = len(nums)-2
        # [1,2,0,1,0]
        #  0 1 2 3 4
        # keep track of the goal = ie n + 1
        # if we can reach it, decrement goal, if no

        curr = len(nums)-2
        goal = curr + 1

        while curr >= 0 and goal >= 0:
            print(nums[curr],nums[goal])
            if nums[curr] >= (goal-curr):# feasible
                goal = curr
            curr -= 1
            
        print(curr,goal)


        return goal == 0

        
            

