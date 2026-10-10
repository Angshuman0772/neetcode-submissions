# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
                
            # Recursively get the best gain from the left and right subtrees.
            #
            # If a subtree gives a negative gain, ignore it by using 0 instead.
            # Adding a negative path would only make the total sum smaller.
            left = max(dfs(node.left) , 0)
            right = max(dfs(node.right) , 0)

            current_sum = left + right + node.val
            max_sum = max(max_sum, current_sum)
            
            # return the current sum to the parent node and build it up
            return node.val + max(left, right)
            
        dfs(root)
        return max_sum