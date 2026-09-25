class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        longest_start_index = 0
        longest_len = 1

        n = len(s)

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1] == True):
                    dp[i][j] = True
                    
                    if j - i + 1 > longest_len:
                        longest_start_index = i
                        longest_len = j - i + 1
        
        return s[longest_start_index : longest_start_index + longest_len]

