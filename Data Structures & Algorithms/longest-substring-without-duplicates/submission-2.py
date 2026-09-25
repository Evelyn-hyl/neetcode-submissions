class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = defaultdict(int)
        l = r = 0
        res = 0

        while r in range(len(s)):
            if s[r] in window:
                l = max(l, window[s[r]] + 1)
            window[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        
        return res
