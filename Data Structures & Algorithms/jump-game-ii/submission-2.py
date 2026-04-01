class Solution:
    def jump(self, nums: List[int]) -> int:
        # [2,1,2,1,0]
        # 
        steps = 0
        l,r = 0,0
        # keep track of farthest
        while l < len(nums) and r < len(nums)-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest,nums[i])
            l = r + 1
            r += farthest
            steps += 1

        return steps