import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # build a min heap of distances between points and 0,0
        # pop k times from the min heap
        d = []
        heapq.heapify(d)
        res = []

        for x,y in points:
            dist = math.sqrt((x ** 2) + (y ** 2))
            if len(d) < k:
                heapq.heappush(d, (-dist, [x,y]))
            elif len(d) and -dist > d[0][0]:
                heapq.heappop(d)
                heapq.heappush(d, (-dist, [x,y]))

        while len(d):
            res.append(heapq.heappop(d)[1])

        return res
        
