class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #naive approach - run a double for loop and multiply the other elements that
        #are not nums[i] together and add that to the result
        
        res = []
        #use a prefix and suffix array
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        #create the prefix array
        p = 1
        for i in range(1,len(nums)):
            p *= nums[i-1]
            prefix[i] = p
        #create the suffix array
        s = 1
        for i in range(len(nums)-2,-1,-1):
            s *= nums[i+1]
            suffix[i] = s
        
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        
        return res