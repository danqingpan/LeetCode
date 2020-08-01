# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
        
        if not root:
            return 0
        
        def recur(root,m):
            if root.left == None and root.right == None and m == 1:
                self.sum += root.val
                return
            if root.left:
                recur(root.left,1)
            if root.right:
                recur(root.right,0)
        
        recur(root,0)
        
        return self.sum