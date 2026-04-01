import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [1,2,3,4] sum = 10 h = 9
        # we want to search from 1 to max(piles), from here 
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
                minTime = min(mid, minTime)
                hi = mid - 1

        return minTime
                

            
        # for k in range(1, max(piles)+1):
        #     time = 0
        #     for p in piles:
        #         time += math.ceil(p / k)
        #     if time <= h:
        #         return k

        # return -1

        
