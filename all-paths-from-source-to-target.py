"""Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

Example 3:
Input: graph = [[1],[]]
Output: [[0,1]]

Example 4:
Input: graph = [[1,2,3],[2],[3],[]]
Output: [[0,1,2,3],[0,2,3],[0,3]]

Example 5:
Input: graph = [[1,3],[2],[3],[]]
Output: [[0,1,2,3],[0,3]]"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        paths = [[0]]
        
        while paths:
            temp = []
            for path in paths:
                if path[-1] == n - 1:
                    ans.append(path)
                for node in graph[path[-1]]:
                    temp.append(path + [node])
            
            paths = temp
            
        return ans

"""Runtime: 100 ms, faster than 78.74% of Python3 online submissions for All Paths From Source to Target.
Memory Usage: 16 MB, less than 13.43% of Python3 online submissions for All Paths From Source to Target."""
                