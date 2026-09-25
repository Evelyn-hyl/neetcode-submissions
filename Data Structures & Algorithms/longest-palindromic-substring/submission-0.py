class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        # Two pointers to collect repeating letters into a dictionary
        # e.g., {'b':[0, 2], 'a':[1, 3]}
        repeat_checker : set[str] = set()
        substrings : dict[str, list[int]] = {}
        i = 0
        longest_substr_len = 1
        longest_substr_ind = 0

        # Collect repeating letters for potential palindromes
        while i < len(s):
            if s[i] in repeat_checker:
                if s[i] not in substrings:
                    substrings[s[i]] = []
                substrings[s[i]].append(i)
            else:
                repeat_checker.add(s[i])
            
            i += 1

        # Go through the substrings dict
        for char, indices in substrings.items():
            # We need to find the first occurrence to check the range
            first_occurrence = s.find(char)
            for end_idx in indices:
                start_idx = first_occurrence
                # Minimal check for all pairs starting from the first occurrence
                while start_idx < end_idx:
                    substring_len = end_idx - start_idx + 1

                    if substring_len > longest_substr_len:
                        sub = s[start_idx : end_idx + 1]
                        if sub == sub[::-1]:
                            longest_substr_len = substring_len
                            longest_substr_ind = start_idx
                    
                    # Check other possible start indices if they exist
                    next_start = s.find(char, start_idx + 1, end_idx)
                    if next_start == -1: break
                    start_idx = next_start
        
        return s[longest_substr_ind : longest_substr_ind + longest_substr_len]
