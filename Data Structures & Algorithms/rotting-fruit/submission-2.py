class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #first get all the rotten fruits, from there do a
        #bfs and mark its neighbours as rotten and keep
        #track of the minutes
        #if fresh set is empty, return

        fresh = set()
        rotten = set()
        q = deque()
        minutes = 0


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh.add((r,c))
                if grid[r][c] == 2:
                    rotten.add((r,c))
                    q.append([r,c])
        
        def markRotten(row,col):
            if (row < 0 or col < 0 or row >= len(grid) 
                or col >= len(grid[0]) or grid[row][col] != 1):
                return
            
            grid[row][col] = 2
            fresh.remove((row,col))
            q.append([row,col])

        #do a bfs on the rotten ones, mark all neighbours as rotten,
        #ie remove them from the fresh and add to rotten
        while q and fresh:
            for i in range(len(q)):
                r,c = q.popleft()
                markRotten(r - 1,c)
                markRotten(r + 1,c)
                markRotten(r,c - 1)
                markRotten(r,c + 1)

            minutes += 1
            print(fresh)

        if len(fresh):
            return -1
        
        return minutes
            