class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Valid graphs cannot have more edges than nodes
        if len(edges) > (n - 1):
            return False
        
        # Build adjacency_list
        adjacency_list = collections.defaultdict(list)
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        visited = set()

        def dfs(node, parent):
            # Cycle detected; not a valid tree
            if node in visited:
                return False
            
            visited.add(node)

            # Skipping the parent node we just came from avoids the false positive loop detection
            for n in adjacency_list[node]:
                if n == parent:
                    continue
                
                # Recursively check neighbors
                if not dfs(n, node):
                    return False
                
            return True

        return dfs(0, -1) and len(visited) == n