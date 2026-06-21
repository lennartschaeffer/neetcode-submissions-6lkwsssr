import copy

class NumMatrix:
    """
    """
    def __init__(self, matrix: List[List[int]]):
        self.m = matrix
        self.c = copy.deepcopy(matrix)
        self.ROWS = len(self.c)
        self.COLS = len(self.c[0])

        for i in range(self.ROWS):
            for j in range(self.COLS):
                if i > 0:
                    self.c[i][j] += self.c[i-1][j]
                if j > 0:
                    self.c[i][j] += self.c[i][j-1]
                    if i > 0:
                        self.c[i][j] -= self.c[i-1][j-1]
                    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.c[row2][col2]
        if row1 > 0:
            total -= self.c[row1-1][col2]
        if col1 > 0:
            total -= self.c[row2][col1-1]
        
        if row1 > 0 and col1 > 0:
            total += self.c[row1-1][col1-1]

        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)