class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = defaultdict(int)
        
        for c in s:
            chars[c] += 1
        
        for i, c in enumerate(s):
            if chars[c] == 1:
                return i
        return -1