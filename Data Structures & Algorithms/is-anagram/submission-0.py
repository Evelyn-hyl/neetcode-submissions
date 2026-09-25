class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        length = len(s)

        s_dict = {}
        t_dict = {}

        for i in range(length):
            if s[i] not in s_dict:
                s_dict.update({s[i] : 1})
            else:
                s_dict[s[i]] += 1
            
            if t[i] not in t_dict:
                t_dict.update({t[i] : 1})
            else:
                t_dict[t[i]] += 1
        
        if t_dict == s_dict:
            return True
        
        return False
        