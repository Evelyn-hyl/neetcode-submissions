class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row_dim = len(heights)
        col_dim = len(heights[0])
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = []

        pacific = set() # Stores visited/pacific-reachable coords
        atlantic = set() # Stores visited/atlantic-reachable coords

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in d:
                if r+dr in range(row_dim) and c+dc in range(col_dim):
                    if heights[r+dr][c+dc] >= heights[r][c] and (r+dr, c+dc) not in visited:
                        dfs(r+dr, c+dc, visited)


        # Top Bottom Rows
        for c in range(col_dim):
            dfs(0, c, pacific)
            dfs(row_dim-1, c, atlantic)
        
        for r in range(row_dim):
            dfs(r, 0, pacific)
            dfs(r, col_dim-1, atlantic)
        
        for item in pacific:
            if item in atlantic:
                result.append(item)

        return result
