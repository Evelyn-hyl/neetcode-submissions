class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        longest = 0
        if s:
            longest += 1

        while r < len(s):
            if s[l] == s[r]:
                l += 1
            else:
                if s[l] in s[l+1:r] or s[r] in s[l+1:r]:
                    l = r
                    r += 1
                    continue

                longest = max(longest, r - l + 1) 
            
            r += 1
        
        return longest