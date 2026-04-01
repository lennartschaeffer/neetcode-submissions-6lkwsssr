class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        

        #loop through the array, check if the num-1 is in the set, if not, start a sequence
        # [2,20,4,19,18,3,4,5]
        # start seq @ 2
        # start seq @ 20
        longest = 0

        for n in nums:
            count = 1
            if n-1 not in numsSet: #indicates the start of a sequence
                curr = n
                while curr + 1 in numsSet:
                    count += 1
                    curr += 1
                if count > longest:
                    longest = count
                count = 0

        return longest

            

        
