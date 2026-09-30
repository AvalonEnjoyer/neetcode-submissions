class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if not (board[r][c]=="X") and (r==0 or r==ROWS-1 or c==0 or c==COLS-1):
                    q.append((r,c))
                    board[r][c]="T"

        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or board[nr][nc]!="O":
                    continue
                board[nr][nc]="T"
                q.append((nr,nc))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c]=="T":
                    board[r][c]="O"
