class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs, keep track of the area, for each iteration
        # check if the current area is greater than max

        def dfs(row,col):

            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return 0
            if grid[row][col] == 0:
                return 0

            grid[row][col] = 0

            area = 1

            area += dfs(row + 1,col) 
            area += dfs(row - 1,col)
            area += dfs(row,col + 1)
            area += dfs(row,col - 1)

            return area
            
        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea,dfs(i,j))

        return maxArea


