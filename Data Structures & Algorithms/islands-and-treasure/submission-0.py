class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        queue = deque()

        def addCell(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited or grid[r][c] == -1):
                return
            visited.add((r, c))
            queue.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r,c])
                    visited.add((r, c))
        
        distance = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = distance
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            distance += 1