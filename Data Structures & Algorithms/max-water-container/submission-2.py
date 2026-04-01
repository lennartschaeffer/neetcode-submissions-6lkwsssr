class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force solution 
        # maxHeight = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         height = min(heights[i],heights[j]) * abs(i-j)
        #         if height > maxHeight:
        #             maxHeight = height
        
        # return maxHeight

        # two pointers, if left < right, increment left
        maxHeight = 0
        left, right = 0, len(heights)-1

        while left < right:
            height = min(heights[left],heights[right]) * abs(left-right)
            if height > maxHeight:
                maxHeight = height

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1 
            


        return maxHeight


