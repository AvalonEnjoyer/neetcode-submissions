class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        q = deque()
        visited=set()
        for r in range(ROWS):
            for c in range(COLS):
                if not (board[r][c]=="X") and (r==0 or r==ROWS-1 or c==0 or c==COLS-1):
                    q.append((r,c))

        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (not(nr<0 or nc<0 or nr>=ROWS or nc>=COLS or 
                    (nr,nc) in visited)) and board[nr][nc]=="O":
                    visited.add((nr,nc))
                    q.append((nr,nc))
            visited.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited:
                    board[r][c]="X"

