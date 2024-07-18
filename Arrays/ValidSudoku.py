class Solution(object):
    def isValidSudoku(self, board):
        #Use hashset for O(1) .contains() operations
        seen = set()

        #Ok to use nested for loop as there are always 81 grid pieces
        for i in range(9):
            for j in range(9):
                #Only look at numbers not empty spaces
                if board[i][j] != ".":
                    #corresponds each number to its row 
                    row = str(i) + "(" + str(board[i][j]) + ")"
                    #corresponds each number to its column
                    col = "(" + str(board[i][j]) + ")" + str(j)
                    #corresponds each number to its 3x3 square
                    grid_piece = str(i / 3) + "(" + str(board[i][j]) + ")" + str(j / 3)
                    
                    #checks if the column, row, or 3x3 grid contains any duplicate numbers
                    if row in seen or col in seen or grid_piece in seen: return False
                    seen.add(row)
                    seen.add(col)
                    seen.add(grid_piece)
                    
        return True

        
