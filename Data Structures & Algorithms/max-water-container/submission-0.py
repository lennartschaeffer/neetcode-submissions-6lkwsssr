class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force solution 
        maxHeight = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                height = min(heights[i],heights[j]) * abs(i-j)
                if height > maxHeight:
                    maxHeight = height
        
        return maxHeight

