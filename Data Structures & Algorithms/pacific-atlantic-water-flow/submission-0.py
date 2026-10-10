class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        # Cells from which water can reach each ocean.
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prevHeight):
            """
            Reverse-flow DFS: start at an ocean-adjacent cell and walk inland,
            only stepping to neighbors that are >= the cell we came from.
            (Going uphill in reverse == going downhill in real water flow.)

            r, c       : current cell
            visited    : the set to fill (pacific OR atlantic)
            prevHeight : height of the cell we just came from
            """
            # Base case 1: stepped outside the grid
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS):
                return

            # Base case 2: already reached from this ocean, avoid loops/rework
            elif (r, c) in visited:
                return

            # Base case 3: current cell is LOWER than where we came from.
            # Real water would have to flow uphill from here into the previous
            # cell, which is impossible, so this cell can't drain that way.
            elif heights[r][c] < prevHeight:
                return

            # Valid: water from this cell can reach the ocean via prev cell
            visited.add((r, c))

            # Explore all 4 neighbors, passing THIS cell's height as their
            # prevHeight (the "previous" cell for them is the current one)
            dfs(r + 1, c, visited, heights[r][c])  # down
            dfs(r - 1, c, visited, heights[r][c])  # up
            dfs(r, c + 1, visited, heights[r][c])  # right
            dfs(r, c - 1, visited, heights[r][c])  # left

        # Start from left (Pacific) and right (Atlantic) borders, row by row.
        # Passing the cell's own height as prevHeight makes the height check
        # pass automatically: border cells touch the ocean, so they always drain.
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])                  # left column  -> Pacific
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])   # right column -> Atlantic

        # Start from top (Pacific) and bottom (Atlantic) borders, column by column
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])                  # top row    -> Pacific
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])   # bottom row -> Atlantic

        # Answer = cells that appear in BOTH reachable sets
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result