# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, minAllowed, maxAllowed):
            if not node:
                return True
            
            if not (minAllowed < node.val < maxAllowed):
                return False
            
            return (valid(node.left, minAllowed, node.val) and
                    valid(node.right, node.val, maxAllowed))
        
        return valid(root, float("-inf"), float("inf"))