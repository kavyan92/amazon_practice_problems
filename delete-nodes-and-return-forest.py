"""Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

Example 1:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Example 2:
Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]"""

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        # create list to store new tree
        ans = []
        # make list of nodes to delete into a set
        to_delete = set(to_delete)
        
        # create a helper method to check each node to the left and right of current node
        def checkTree(root):
            # if node is empty, return none
            if not root:
                return None
            
            # call helper method on node to left and right
            root.left = checkTree(root.left)
            root.right = checkTree(root.right)
            
            # if node value is in to_delete, add any child nodes to the result list, then return none
            if root.val in to_delete:
                if root.left:
                    ans.append(root.left)
                if root.right:
                    ans.append(root.right)
                return None
            # else return root
            return root
        
        # if starting node value is not to be deleted, add it to result list
        if root.val not in to_delete:
            ans.append(root)
        # call helper method on starting node for DFS
        checkTree(root)
        
        # return result list
        return ans

"""Runtime: 68 ms, faster than 75.33% of Python3 online submissions for Delete Nodes And Return Forest.
Memory Usage: 15 MB, less than 26.20% of Python3 online submissions for Delete Nodes And Return Forest."""