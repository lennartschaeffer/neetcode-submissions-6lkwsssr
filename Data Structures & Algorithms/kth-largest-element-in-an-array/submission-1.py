import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #[5,4], k = 2
        #heapify this o(n)
        # while len < k, pop
        # pop - that should be kth largest
        # logn
        h = []
        heapq.heapify(h)

        for n in nums: # o(n)
            heapq.heappush(h,n) #o(log k)
            if len(h) > k: 
                heapq.heappop(h) #o log k
            print(h)

        return h[0] # o(1)


