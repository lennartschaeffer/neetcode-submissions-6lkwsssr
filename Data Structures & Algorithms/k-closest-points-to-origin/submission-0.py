import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # build a min heap of distances between points and 0,0
        # pop k times from the min heap
        d = []
        res = []
        i = 0
        for x,y in points:
            dist = math.sqrt((x ** 2) + (y ** 2))
            d.append((dist,i))
            i += 1

        heapq.heapify(d)
        print(d)
        for _ in range(k):
            idx = heapq.heappop(d)[1]
            res.append(points[idx])

        return res
        
