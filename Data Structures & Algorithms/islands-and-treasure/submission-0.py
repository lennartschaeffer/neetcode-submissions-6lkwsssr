class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multi source bfs go through the list and get all the 
        # treasure chests, from there mark all their closest 
        # land cells
        q = deque()
        seen = set()
        dist = 0

        def markDist(r,c):
            if ((r,c) in seen or r < 0 or c < 0 or r >= len(grid)
            or c >= len(grid[0]) or grid[r][c] == -1):
                return

            grid[r][c] = dist
            q.append([r,c])
            seen.add((r,c))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append([r,c])
                    seen.add((r,c))

        
        while q:
            dist += 1
            for i in range(len(q)):
                r,c = q.popleft()
                markDist(r-1,c)
                markDist(r+1,c)
                markDist(r,c-1)
                markDist(r,c+1)












        

            
