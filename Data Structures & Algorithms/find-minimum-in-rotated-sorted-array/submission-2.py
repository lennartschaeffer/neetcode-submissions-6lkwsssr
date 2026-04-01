class Solution:
    def findMin(self, nums: List[int]) -> int:
        # were gonna use binary search, and how well approach this is

        lo, hi = 0, len(nums)-1
        minNum = nums[0]

        while lo <= hi:
            if nums[lo] < nums[hi]:
                minNum = min(minNum,nums[lo])
                break

            mid = (lo+hi) // 2
            minNum = min(minNum,nums[mid])

            if nums[lo] <= nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1

        return minNum

        
            

            