"""Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []"""

class Node:
    def __init__(self, end = 0):
        self.end = end
        self.kids = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, root, m, n = set(), Node(0), len(board), len(board[0])
        
        def setTrie(word):
            cur = root
            for w in word:
                if w not in cur.kids:
                    cur.kids[w] = Node()
                cur = cur.kids[w]
            cur.end = 1
            return
        
        def helper(i, j, root, visited, word):
            if root.end == 1: res.add(word)
            visited.add((i, j)) 

            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                x, y = i + dx, j + dy
                if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visited or board[x][y] not in root.kids: continue
                helper(x, y, root.kids[board[x][y]], visited, word + board[x][y])
            visited.remove((i, j))

            return        
        
        for word in words: setTrie(word)

        for i in range(m):
            for j in range(n):
                if board[i][j] in root.kids: helper(i, j, root.kids[board[i][j]], set(), board[i][j])         
                
        return list(res)