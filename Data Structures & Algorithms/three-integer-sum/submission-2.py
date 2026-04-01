class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4,-1,-1,0,1,2]
        
        #sort the array
        nums.sort()
        # from there, loop through each element, then use two pointers on the array elements
        # to the right, and check if all 3 add up to zero
        res = []

        for i in range(len(nums)):
            # make sure to skip duplicates

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1
            
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    #to prevent duplicates, make sure left pointer moves past any duplicates
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return res
