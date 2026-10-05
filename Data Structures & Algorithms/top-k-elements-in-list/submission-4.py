class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            solutsion:
                count frequencies with hashmap, O(N)
                sort values (NlogN)
                take top k => NlogN solution
                what if we add all frequencies onto a heap
                We can get O(N + klogN)
        """ 
        d = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for key,val in d.items():
            buckets[val].append(key)
        took = 0
        res = []
        for i in range(len(buckets)-1,0,-1):
            for j in range(len(buckets[i])):
                if took == k:
                    return res
                res.append(buckets[i][j])
                took += 1
        return res
        

