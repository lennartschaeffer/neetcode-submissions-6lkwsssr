class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(row, col, ltrIdx):
            if ltrIdx == len(word):
                return True
            if row < 0 or row >= len(board): 
                return False
            if col < 0 or col >= len(board[0]):
                return False
            if board[row][col] != word[ltrIdx] or board[row][col] == '#':
                return False
            
            board[row][col] = '#'

            res = (backtrack(row + 1, col, ltrIdx + 1) or
            backtrack(row - 1, col, ltrIdx + 1) or 
            backtrack(row, col + 1, ltrIdx + 1) or 
            backtrack(row, col - 1, ltrIdx + 1))

            board[row][col] = word[ltrIdx]

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return True

        return False
            


            