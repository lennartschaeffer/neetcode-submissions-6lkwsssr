class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seen = set()
        lengths = {}
        maxLen = 0
        minVal = float('inf')

        for n in nums:
            seen.add(n)
            lengths[n] = 0
            minVal = min(minVal,n)
            for i in range(minVal,n):
                if i in seen:
                    print(n,i,lengths[i],lengths[n])
                    lengths[n] = max(lengths[i],lengths[n])
            lengths[n] += 1
            maxLen = max(maxLen,lengths[n])

        print(lengths)
        
        return maxLen
