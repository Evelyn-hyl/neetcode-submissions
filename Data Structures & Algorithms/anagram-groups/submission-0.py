class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map : dict[int, List[str]] = {}

        for i in range(len(strs)):
            hash_num = hash("".join(sorted(strs[i])))
            if hash_num not in hash_map:
                hash_map[hash_num] = []
                hash_map[hash_num].append(strs[i])
                continue
            hash_map[hash_num].append(strs[i])

        return list(hash_map.values())

        