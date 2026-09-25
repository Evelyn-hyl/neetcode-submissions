from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_dim = len(grid)
        col_dim = len(grid[0])
        q = deque()
        total_min = 0
        fresh = 0
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(row_dim):
            for c in range(col_dim):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        while fresh > 0 and q:
            q_len = len(q)

            for i in range(q_len):
                r, c = q.popleft()
                for dr, dc in d:
                    if r+dr < 0 or c+dc < 0 or r+dr >= row_dim or c+dc >= col_dim:
                        continue
                    
                    if grid[r+dr][c+dc] == 1:
                        q.append((r+dr, c+dc))
                        grid[r+dr][c+dc] = 2
                        fresh -= 1
                    
            total_min += 1
        
        return total_min if fresh == 0 else -1
                    
                
                    
        
                    
            
            