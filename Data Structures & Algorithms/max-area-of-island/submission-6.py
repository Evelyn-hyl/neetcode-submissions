class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        edges = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        row_dim = len(grid)
        col_dim = len(grid[0])
        max_area = 0

        def dfs(row, col, a):
            # Base Case
            if row < 0 or col < 0 or row >= row_dim or col >= col_dim or grid[row][col] == 0:
                return a;
            
            a += 1
            grid[row][col] = 0

            area = 0

            for r, c in edges:
                area += dfs(row + r, col + c, 0)
            
            return a + area
                    
        for r in range(row_dim):
            for c in range(col_dim):
                if grid[r][c] == 1:
                    a = dfs(r, c, 0)
                    max_area = max(a, max_area)
                    curr_area = 0

        return max_area