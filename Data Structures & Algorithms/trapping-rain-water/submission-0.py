class Solution:
    def trap(self, height: List[int]) -> int:
        #brute force, for each element, get the two biggest heights to the left and right
        totalWater = 0
        for i in range(len(height)):
            #find the max left height and right height
            maxLeft,maxRight = 0,0
            for j in range(i):
                maxLeft = max(maxLeft, height[j])
            for k in range(i+1, len(height)):
                maxRight = max(maxRight, height[k])
            
            #get the amount of water
            water = min(maxRight, maxLeft) - height[i]
            print(maxLeft,maxRight,water)
            if water > 0:
                totalWater += water

        return totalWater