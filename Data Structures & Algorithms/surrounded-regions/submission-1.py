class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def capture(r, c):
            # out of bounds
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS):
                return
            # already captured
            if (board[r][c] != 'O'):
                return
            # We mark as T every 'O' cell that is connected to the border
            board[r][c] = 'T'
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        
        # Run capture from every border cell that is 'O'
        for r in range(ROWS):
            if board[r][0] == 'O':
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)
        
        for c in range(COLS):
            if board[0][c] == 'O':
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)
        
        # Scan entire board
        for r in range(ROWS):
            for c in range(COLS):
                # If cell is still 'O', it's surrounded → change to 'X'.
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                # If cell is 'T', it's safe → change back to 'O'
                elif board[r][c] == "T":
                    board[r][c] = "O"