"""Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # initialize empty list to keep track of each levels sum
        ans = []
        # if root node is empty, return 0
        if not root:
            return 0
        
        # create list(queue) with root node
        queue = [root]
        
        # while the queue is not empty, first get length of queue (which is the number of nodes in each level)
        while queue:
            n = len(queue)
            # initialize var to keep track of sum
            level_sum = 0
            # loop through each node in that level and add it to level_sum
            # if they have child nodes, add it to the back of the queue
            for i in range(n):
                node = queue.pop(0)
                level_sum += (node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # add the sum to the result list
            ans.append(level_sum)
        
        # find the max sum in result list
        m = max(ans)
        
        # return the index of that max value
        return ans.index(m) + 1