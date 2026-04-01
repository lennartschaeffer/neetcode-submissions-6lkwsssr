class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        maxHeap = []
        heapq.heapify(maxHeap)

        for i in range(k-1):
            heapq.heappush(maxHeap, (-nums[i], i))
        
        for r in range(k-1,len(nums)):
            heapq.heappush(maxHeap,(-nums[r],r))
            #get max from max heap
            while len(maxHeap):
                maxNum, idx = maxHeap[0]
                if l <= idx <= r:
                    res.append(-maxNum)
                    break
                else:
                    heapq.heappop(maxHeap)

            l += 1

        return res