class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = defaultdict(list[int])

        for i in range(len(s)):
            if s[i] in chars:
                chars[s[i]] = []
                continue
            chars[s[i]].append(i)
        
        for char in chars:
            if chars[char]:
                return chars[char][0]
        
        return -1
        