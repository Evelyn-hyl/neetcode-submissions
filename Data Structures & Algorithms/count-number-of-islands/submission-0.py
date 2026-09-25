class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_dim = len(grid)
        col_dim = len(grid[0])
        groups = 0

        def dfs(row, col):
            # Base case
            if col < 0 or row < 0 or col >= col_dim or row >= row_dim or grid[row][col] == '0':
                return;

            grid[row][col] = '0'

            # Explore all four edges
            for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(row + r, col + c)
            
        for r in range(row_dim):
            for c in range(col_dim):
                if grid[r][c] == '1':
                    groups += 1
                    dfs(r, c)
        
        return groups
                
            