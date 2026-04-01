class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        
        def dfs(r,c):
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0])
            or board[r][c] == 'X' or board[r][c] == '#'):
                return

            board[r][c] = '#'

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(len(board)):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][len(board[0])-1] == 'O':
                dfs(i,len(board[0])-1)

        for i in range(len(board[0])):
            if board[0][i] == 'O':
                dfs(0,i)
            if board[len(board)-1][i] == 'O':
                dfs(len(board)-1,i)    

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

        
