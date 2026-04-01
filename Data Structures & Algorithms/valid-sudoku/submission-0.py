class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #use hash set to check for duplicates within rows or columns
        #there are 9 squares, so you a hashmap where each index 0-8 will correspond 
        #to the index of the square. Like {0: set(1,4,6,7)} same thing for rows and columns

        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                # add the value to it's hashmap
                val = board[i][j]
                if val not in rows[i] and val not in columns[j] and val not in squares[(i//3,j//3)]:
                    if val.isnumeric():
                        rows[i].add(val)
                        columns[j].add(val)
                        squares[(i//3,j//3)].add(val)
                else:
                    # print(i, rows[i])
                    # print(j, columns[j])
                    # print(squaresIdx, squares[squaresIdx])
                    return False

        return True
        

        

