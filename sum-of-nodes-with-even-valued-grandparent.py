"""Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.

Example 1:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.

Example 2:
Input: root = [1]
Output: 0"""

class Solution:
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # intialize variable to keep track of sum
        self.ans = 0
        
        # call helper method on root node
        self.helper(root, to_add=False)
        # return total sum
        return self.ans
    
    # define helper method to recurse through tree
    def helper(self, root, to_add=False):
        # if root is empty, return none
        if not root:
            return None
        # if root node is even, add to sum
        if to_add:
            self.ans += root.val
            return
        # check if root node is even, if so, traverse to grandchild nodes and set to True
        if root.val % 2 == 0:
            if root.left:
                self.helper(root.left.left, to_add=True)
                self.helper(root.left.right, to_add=True)

            if root.right:
                self.helper(root.right.right, to_add=True)
                self.helper(root.right.left, to_add=True)
        # call helper method on child nodes and traverse through their grandchildren        
        self.helper(root.left, to_add=False)
        self.helper(root.right, to_add=False)

"""Runtime: 192 ms, faster than 7.55% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
Memory Usage: 17.6 MB, less than 92.99% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent."""