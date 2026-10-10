class Solution:
    def findRedundantConnection(self, edges: List[List[int]]):

        graph = collections.defaultdict(list)

        def dfs(src, target, visited):
            if src == target:
                return True

            visited.add(src)

            for nei in graph[src]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True

            return False

        for u, v in edges:

            visited = set()

            # If both nodes already connected,
            # adding this edge forms a cycle.
            if u in graph and v in graph:
                if dfs(u, v, visited):
                    return [u, v]

            graph[u].append(v)
            graph[v].append(u)

        return []