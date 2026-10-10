class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = {}
        res = 0
        l = 0

        for r in range(n):
            if s[r] in seen:
                # move the left pointer
                l = max(l, seen[s[r]]+1)
            
            res = max(res, r-l+1)
            seen[s[r]] = r

        return res