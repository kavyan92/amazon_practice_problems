"""Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Example 1:
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Example 2:
Input: board = [["."]]
Output: 0"""

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # initialize counter variable
        count = 0
        # loop through each 'row' in board
        for row in range(len(board)):
            # loop through each 'column' within each row
            for column in range(len(board[0])):
                # if you find an X, check the squares next to it. 
                # if they are . then increment counter
                if board[row][column] == 'X' and (row == 0 or board[row-1][column] == '.') and (column == 0 or board[row][column-1] == '.'):
                    count += 1
        
        # return count
        return count

"""Runtime: 64 ms, faster than 97.68% of Python3 online submissions for Battleships in a Board.
Memory Usage: 14.6 MB, less than 92.65% of Python3 online submissions for Battleships in a Board."""