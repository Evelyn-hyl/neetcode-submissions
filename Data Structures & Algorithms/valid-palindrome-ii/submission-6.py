class Solution:
    def validPalindrome(self, s: str) -> bool:
        deleted = 0
        l, r = 0, len(s) - 1

        def isPalindrome(l, r):
            while r > l:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True

        while r > l:
            if s[r] != s[l]:
                return (isPalindrome(l+1, r) or isPalindrome(l, r-1))
            
            l += 1
            r -= 1
        
        return True