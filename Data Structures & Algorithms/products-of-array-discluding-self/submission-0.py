class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #naive approach - run a loop to get the total product
        #now run a second loop and append totalProduct / nums[i]

        res = []

        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if j != i:
                    total *= nums[j]
            res.append(total)
            total = 1
        

        return res