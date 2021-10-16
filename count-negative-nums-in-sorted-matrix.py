"""Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # initialize a counter var
        neg = 0
        # start loop to iterate through each list within grid
        for row in grid:
            # start loop to iterate through each num in inner list
            for num in row:
                # if it's below 0, increment counter
                if int(num) < 0:
                    neg += 1
        # return counter
        return neg

"""Runtime: 124 ms, faster than 53.68% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
Memory Usage: 15 MB, less than 75.74% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix."""