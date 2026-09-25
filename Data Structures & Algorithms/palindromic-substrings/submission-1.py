class Solution:
    def countSubstrings(self, s: str) -> int:
        s_len = len(s)
        res = []

        def findPalindromes(l, r):
            nonlocal res, s_len
            while l >= 0 and r < s_len and s[l] == s[r]:
                res.append(s[l: r+1])
                l -= 1
                r += 1
        
        for i in range(s_len):
            # Even Length
            findPalindromes(i, i+1)

            # Odd Length
            findPalindromes(i, i)
        
        return len(res)
