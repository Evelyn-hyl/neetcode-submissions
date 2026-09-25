class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        lower_s = s.lower()

        while i < j:
            ascii_i = ord(lower_s[i])
            ascii_j = ord(lower_s[j])
            
            if not 97 <= ascii_i <= 122 and not 48 <= ascii_i <= 57:
                i += 1
                continue
            if not 97 <= ascii_j <= 122 and not 48 <= ascii_j <= 57:
                j -= 1
                continue
            
            if lower_s[i] != lower_s[j]:
                return False
            
            i += 1
            j -= 1
        
        return True