class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols):
                return
            
            if grid[r][c] == '0':
                return
            
            pos = (r, c)

            if pos in visited:
                return
            
            visited.add(pos)

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    count += 1
        
        return count
