# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []

        queue = deque([root])

        while queue:
            right_side_element = None
            queueLength = len(queue)

            for i in range(queueLength):
                node = queue.popleft()

                right_side_element = node

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(right_side_element.val)
        
        return result