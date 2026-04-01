class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # starting from each 0 i.e. treasure chest, we do a bfs
        # and keep track of the level we're at (1 being the closest, then 2...)
        # one thing we might also have to do is to check:
        # is land < currentLevel, because if not, it means there already a closer treasure
        ROWS = len(grid)-1
        COLS = len(grid[0])-1

        def bfs(r,c):
            seen = set()
            q = deque()
            q.append((r,c))
            distance = 1
            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            while len(q):
                n = len(q)
                for i in range(n):
                    row,col = q.popleft()
                    seen.add((row,col))
                    for dr, dc in directions:
                        newRow = row + dr
                        newCol = col + dc
                        if newRow < 0 or newRow > ROWS or newCol < 0 or newCol > COLS:
                            continue
                        if ((newRow, newCol) in seen or
                            grid[newRow][newCol] == -1 or grid[newRow][newCol] == 0):
                            continue
                        
                        grid[newRow][newCol] = min(distance, grid[newRow][newCol])
                        q.append((newRow,newCol))

                distance += 1

        for i in range(ROWS+1):
            for j in range(COLS+1):
                if grid[i][j] == 0:
                    bfs(i,j)
                    





