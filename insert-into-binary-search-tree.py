"""You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

Example 1:


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]"""

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if root is empty, return tree with val as root node
        if not root:
            return TreeNode(val)
        # if val is less than the root node, call the same method on the left child node
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        # if val is greater than root node, call method on the right child node
        else:
            root.right = self.insertIntoBST(root.right, val)
            
        # return new tree
        return root

