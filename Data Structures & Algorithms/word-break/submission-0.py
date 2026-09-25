class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        max_len = max(len(w) for w in wordDict)
        wordSet = set(wordDict)

        for i in range(1, n+1):
            for l in range(1, max_len + 1):
                if dp[i - l] and s[i-l:i] in wordSet:
                    dp[i] = True

        return dp[n]