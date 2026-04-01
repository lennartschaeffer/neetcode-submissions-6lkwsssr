import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #[5,4], k = 2
        #heapify this o(n)
        # while len < k, pop
        # pop - that should be kth largest
        # logn
        heapq.heapify(nums)
        print(nums, len(nums), k)
        while len(nums) > k:
            heapq.heappop(nums)
            print(nums)

        return nums[0]
