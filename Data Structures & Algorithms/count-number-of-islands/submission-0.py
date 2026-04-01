class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # loop through the grid, and if we encounter a 1,
        # we have to explore all directions where we read ones
        # and mark them as visited, i.e. 0
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if grid[row][col] == "0":
                return

            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    res += 1

        return res

