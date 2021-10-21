"""Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:
Input: root = [0,null,1]
Output: [1,null,1]

Example 3:
Input: root = [1,0,2]
Output: [3,3,2]

Example 4:
Input: root = [3,2,4,1]
Output: [7,9,4,10]"""

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # initialize variable with value to add- start at 0
        to_add = [0]
        # create helper method to recurse through tree
        def helper(root, to_add):
            # if there is no node, return
            if not root:
                return root
            # call helper method on right node if there is one, with to add sum to keep track of greater value nodes
            helper(root.right, to_add)
            # add 'to_add' to the current node val
            root.val += to_add[0]
            # set variable to the new sum
            to_add[0] = root.val
            # call helper method on left node if there is one
            helper(root.left, to_add)
            # return value for new greater sum node
            return root
        
        # call helper method recursively starting at root
        return helper(root, to_add)

"""Runtime: 28 ms, faster than 90.41% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
Memory Usage: 14.1 MB, less than 96.51% of Python3 online submissions for Binary Search Tree to Greater Sum Tree."""