class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q = deque()
        for r in range(ROWS):
            if board[r][0] == "O":
                board[r][0] = "S"
                q.append((r, 0))
            
            if board[r][COLS - 1] == "O":
                board[r][COLS - 1] = "S"
                q.append((r, COLS - 1))
        
        for c in range(COLS):
            if board[0][c] == "O":
                board[0][c] = "S"
                q.append((0, c))
            
            if board[ROWS - 1][c] == "O":
                board[ROWS - 1][c] = "S"
                q.append((ROWS - 1, c))
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (nr >= 0 and nr < ROWS and
                    nc >= 0 and nc < COLS and 
                    board[nr][nc] == "O"):
                    board[nr][nc] = "S"
                    q.append((nr, nc))
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
        






