import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use a max heap
        # while loop for while stones > 1
        # pop twice from the heap, do the comparisons
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = -(heapq.heappop(maxHeap))
            if not len(maxHeap):
                return 0
            y = -(heapq.heappop(maxHeap))
            print(x,y)
            if y < x:
                heapq.heappush(maxHeap, -(x-y))
            print(maxHeap)

        return -maxHeap[0] if len(maxHeap) else 0            
