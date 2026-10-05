class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            solutsion:
                count frequencies with hashmap, O(N)
                sort values (NlogN)
                take top k
                => NlogN solution
                what if we add all frequencies onto a heap
                We can get O(N + klogN)
        """ 
        d = Counter(nums)
        h = []
        for key,val in d.items():
            heapq.heappush(h, (-val,key))
        res = []
        for i in range(k):
            _, key = heapq.heappop(h)
            res.append(key)
        return res

