from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        # Sort by values
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        
        return list(sorted_freq.keys())[0:k]


