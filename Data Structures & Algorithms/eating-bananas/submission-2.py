import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        minTime = max(piles)
        #we can do a binary search from 1 to the max, find the mid point
        #do the calculation for each p in piles, if time <= h and < minTime, update
        #1,2,3,...,25
        lo,hi = 1, max(piles)
        while lo <= hi:
            mid = (lo + hi) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / mid)
            if time > h:
                lo = mid + 1
            else:
                minTime = mid
                hi = mid - 1

        return minTime
                

            
        
        
