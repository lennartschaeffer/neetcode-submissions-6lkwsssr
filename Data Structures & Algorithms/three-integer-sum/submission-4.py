class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,0,1,2,-1,-4]
        # [-4,-1,-1,0,1,2]
        #  i  j         k
        """
        i = 1
        j = 3
        k = 4

        total = 
        """

        nums.sort() # o n log n
        res = []

        for idx,num in enumerate(nums):
            i = idx
            j = i + 1
            k = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

        return res

    