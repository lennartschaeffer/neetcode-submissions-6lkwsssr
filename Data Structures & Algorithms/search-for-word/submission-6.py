class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
            more dfs style approach
            from every source, explore all directions
            if currLetter != nextLetter in word, we can return immediately
            we should use a pointer for word to keep track of which letter we need

            double for loop
                if board[i][j] == currLetter:
                    dfs(i,j)
            
            dfs
                if out of bounds or currLetter != nextLetter in word: return

                inc nextLetter

                dfs left, right, up, down
        """

        ROWS = len(board)
        COLS = len(board[0])
        seen = set()

        def dfs(r,c, nextLetterIdx):
            if (r,c) in seen:
                return False
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or board[r][c] != word[nextLetterIdx]:
                return False
            
            seen.add((r,c))
            nextLetterIdx += 1
            if nextLetterIdx == len(word):
                return True
            
            valid = dfs(r+1,c, nextLetterIdx) \
                    or dfs(r-1,c, nextLetterIdx) \
                    or dfs(r,c+1, nextLetterIdx) \
                    or dfs(r,c-1, nextLetterIdx) \

            seen.remove((r,c))
            return valid
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        
        return False
        