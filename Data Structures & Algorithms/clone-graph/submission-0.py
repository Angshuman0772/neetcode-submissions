"""
import copy
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
        
            nodeCopy = Node(node.val)
            oldToNew[node] = nodeCopy
            for n  in node.neighbors:
                nodeCopy.neighbors.append(dfs(n))
            return nodeCopy
    
        return dfs(node) if node else None