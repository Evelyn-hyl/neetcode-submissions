class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l= 0
        max_len = 0
        window = defaultdict(int)

        for r in range(len(s)):
            if s[r] in window:
                l = max(l, window[s[r]] + 1)
            max_len = max(max_len, r - l + 1)
            window[s[r]] = r
        
        return max_len