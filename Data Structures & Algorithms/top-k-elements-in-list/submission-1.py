class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       numbers_map = {}
       frequency = [[] for i in range(len(nums) + 1)]

       for n in nums:
        numbers_map[n] = 1 + numbers_map.get(n, 0)

       for key,val in numbers_map.items():
        frequency[val].append(key)

       result = []

       for i in range(len(frequency)-1, 0, -1):
        for j in frequency[i]:
            result.append(j)
            if(len(result) == k):
                return result
            
       

       


