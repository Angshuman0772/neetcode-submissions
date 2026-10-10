class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_list = collections.defaultdict(list)
        
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        
        visited = set()
        components = 0

        def dfs(node):
            visited.add(node)

            for nei in adjacency_list[node]:
                if nei not in visited:
                    dfs(nei)

        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1

        return components