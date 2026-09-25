class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        seen = defaultdict(int)
        long_len = 0

        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
                
            seen[s[r]] = r
            long_len = max(r - l + 1, long_len)
        
        return long_len
            
            


        