class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m-1 or c == n-1:
                    dp[r][c] = 1
                    continue
                
                dp[r][c] = dp[r][c+1] + dp[r+1][c]

        return dp[0][0]