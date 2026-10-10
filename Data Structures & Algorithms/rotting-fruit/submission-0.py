class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()
        fresh = 0
        time = 0

        # Find all rotten oranges and count fresh ones
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                # add rotten oranges into the queue
                elif grid[r][c] == 2:
                    queue.append((r, c))

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        # BFS
        while queue and fresh > 0:

            # Process one BFS level (1 minute)
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    # Skip if out of bounds
                    if (
                        row < 0 or row >= ROWS or
                        col < 0 or col >= COLS
                    ):
                        continue

                    # Skip if not a fresh orange
                    if grid[row][col] != 1:
                        continue

                    # Rot the fresh orange
                    grid[row][col] = 2
                    fresh -= 1
                    queue.append((row, col))

            # One minute has passed
            time += 1

        return time if fresh == 0 else -1