"""Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23."""

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # initializ variable to keep track of sum
        in_range = 0
        # if root node is null, return 0
        if not root:
            return 0
        # set up stack with list of root
        stack = [root]
        # while stack is not empty, keep looping
        while stack:
            # intialize var to hold most recent item added to stack as you loop 
            x = stack.pop()
            # if there is a node, check if its within the given range
            if x:
                # if yes, add it to the sum
                if low <= x.val <= high:
                    in_range += x.val
                # if the lower range limit is less than the value, add the node to the left to stack
                if low <= x.val:
                    stack.append(x.left)
                # if the upper range limit is greater than the value, add the node to the right to stack
                if x.val <= high:
                    stack.append(x.right)
        
        # return sum
        return in_range

"""Runtime: 204 ms, faster than 86.23% of Python3 online submissions for Range Sum of BST.
Memory Usage: 22.2 MB, less than 85.47% of Python3 online submissions for Range Sum of BST."""