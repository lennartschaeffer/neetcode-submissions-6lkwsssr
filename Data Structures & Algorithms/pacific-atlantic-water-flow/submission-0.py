class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)-1
        COLS = len(heights[0])-1
        pac_q = deque()
        atl_q = deque()


        def canFlow(r,c,prev,seen):
            if (r < 0 or r > ROWS or c < 0 or c > COLS or heights[r][c] < prev 
                or (r,c) in seen):
                return False
            return True

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == 0 or c == 0:
                    pac_q.append((r,c))
                if r == ROWS or c == COLS:
                    atl_q.append((r,c))

        # can try a bfs for p, get everything that can flow to p
        # same thing for a
        # check which ones overlap
        def bfs(ocean):
            seen = set()
            canFlowOcean = set()
            while ocean:
                row,col = ocean.popleft()
                if canFlow(row-1,col,heights[row][col],seen):
                    ocean.append((row-1,col))
                if canFlow(row+1,col,heights[row][col],seen):
                    ocean.append((row+1,col))
                if canFlow(row,col-1,heights[row][col],seen):
                    ocean.append((row,col-1))
                if canFlow(row,col+1,heights[row][col],seen):
                    ocean.append((row,col+1))
                canFlowOcean.add((row,col))
                seen.add((row,col))

            return canFlowOcean
        
        canFlow_pac = bfs(pac_q)
        canFlow_atl = bfs(atl_q)
        res = []
        for r,c in canFlow_pac:
            if (r,c) in canFlow_atl:
                res.append([r,c])

        return res
