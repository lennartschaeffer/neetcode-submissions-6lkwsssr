class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        double for loop to iterate through 2d array. 
        keep a dict with hashset as the value and key as idx for rows and cols

        for 3x3 sub boxes:
            mod by 9, keep a dict for that as well. 
            there are 9 boxes, so the formula is 

            (row / 3) * 3 + (col / 3)
        """
        if not len(board):
            return True

        ROWS = len(board)
        COLS = len(board[0])

        rows_seen = defaultdict(set)
        cols_seen = defaultdict(set)
        grid_seen = defaultdict(set)

        for i in range(ROWS):
            for j in range(COLS):
                val = board[i][j]
                if val == '.': continue
                grid_idx = (i // 3) * 3 + (j // 3)
                if val in rows_seen[i] or val in cols_seen[j] or val in grid_seen[grid_idx]:
                    print(val)
                    return False
                else:
                    rows_seen[i].add(val)
                    cols_seen[j].add(val)
                    grid_seen[grid_idx].add(val)

        return True
